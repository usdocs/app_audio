import os

from django.http import FileResponse
from django.urls import reverse_lazy
from rest_framework import generics, permissions, status
from rest_framework.authtoken.models import Token
from rest_framework.decorators import api_view
from rest_framework.response import Response

from dotenv import load_dotenv

from api.include.convert_audio import convert_audio
from api.serializers import AudiorecordSerializer, SignUpSerializer
from audiorecords.models import Audiorecord
from users.models import User

load_dotenv()


@api_view(['POST'])
def signup(request):
    """Создает пользователя и выдает токен доступа"""
    serializer = SignUpSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = User.objects.create(
        username=request.data['username'],
    )
    token = Token.objects.create(user=user)
    response = {'token': str(token), 'uuid': str(user.id)}
    return Response(response, status=status.HTTP_200_OK)


class AudiorecordCreate(generics.CreateAPIView):
    """Создает запись в БД с аудиофайлом, конвертирует его и отдает
       ссылку на скачивание"""
    queryset = Audiorecord.objects.all()
    serializer_class = AudiorecordSerializer
    permission_classes = (permissions.IsAuthenticated,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        id_user = request.data['author']
        try:
            user = User.objects.get(id=id_user)
        except Exception as error:
            return Response(
                {f'Ошибка в UUID автора: {error}'},
                status=status.HTTP_400_BAD_REQUEST
            )
        serializer.save(author=user)

        id_record = serializer.data['id']
        convert_audio(id_record)

        host = os.getenv('LOCAL_HOST')
        url = host + reverse_lazy('api:record')
        response = {f'{url}?id={id_record}&user={id_user}'}
        return Response(response, status=status.HTTP_201_CREATED)


@api_view(['GET'])
def download_record(request):
    """Проверяет get параметры и отдает файл на скачивание"""
    if 'id' and 'user' not in request.GET:
        return Response(
            {'Неверные параметры для скачивания'},
            status=status.HTTP_400_BAD_REQUEST
        )

    id_record = request.GET.get('id')
    id_user = request.GET.get('user')

    try:
        user = User.objects.get(id=id_user)
    except Exception as error:
        return Response(
            {f'Ошибка в UUID автора: {error}'},
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        record = Audiorecord.objects.get(id=id_record, author=user)
    except Exception as error:
        return Response(
            {f'Ошибка в UUID записи: {error}'},
            status=status.HTTP_400_BAD_REQUEST
        )

    audio = record.audio
    return FileResponse(audio, as_attachment=True)
