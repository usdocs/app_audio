import os
from django.conf import settings
from django.core.files.base import ContentFile
from rest_framework import status
from rest_framework.response import Response

from pydub import AudioSegment

from audiorecords.models import Audiorecord


def convert_audio(id_record):
    try:
        audiorecord = Audiorecord.objects.get(id=id_record)
    except Exception as error:
        return Response(
            {f'Ошибка в UUID записи: {error}'},
            status=status.HTTP_400_BAD_REQUEST
        )

    filename = str(audiorecord.audio)
    name = os.path.splitext(filename)[0]
    filepath = os.path.join(settings.MEDIA_ROOT, filename)
    record = AudioSegment.from_wav(filepath)
    record_mp3 = record.export(f'media/{name}.mp3', format='mp3')
    print(record_mp3)
    audiorecord.audio.save(f'{name}.mp3', ContentFile(record_mp3.read()))
