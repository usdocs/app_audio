import os
import random
import string

from pydub import AudioSegment


def convert_audio(record):
    filename = str(record)
    name = os.path.splitext(filename)[0]
    random_name = ''.join(random.choice(string.ascii_lowercase)
                          for i in range(7))
    file_name = f'{name}_{random_name}.mp3'
    AudioSegment.from_wav(record).export(f'media/{file_name}', format='mp3')
    return file_name
