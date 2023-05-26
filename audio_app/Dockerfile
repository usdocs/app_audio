FROM python:3.7-slim

WORKDIR /app

COPY requirements.txt ./

RUN pip3 install -r requirements.txt --no-cache-dir

RUN apt-get -y update && apt-get -y upgrade && apt-get install -y --no-install-recommends ffmpeg

COPY ./ ./

CMD ["gunicorn", "audio_app.wsgi:application", "--bind", "0:8000" ]
