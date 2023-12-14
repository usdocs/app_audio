from rest_framework import serializers

from audiorecords.models import Audiorecord
from users.models import User


class SignUpSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username',)


class AudiorecordSerializer(serializers.ModelSerializer):
    author = serializers.CharField(label='Автор')

    class Meta:
        model = Audiorecord
        fields = ('id', 'author', 'audio',)
        read_only_fields = ('id',)
