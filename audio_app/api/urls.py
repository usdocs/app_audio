from django.urls import path

from api.views import AudiorecordCreate, download_record, signup

urlpatterns = [
    path('v1/signup/', signup),
    path('v1/audiorecord/', AudiorecordCreate.as_view()),
    path('record/', download_record, name='record')
]
