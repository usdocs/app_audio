from api.views import AudiorecordCreate, download_record, signup
from django.urls import path

urlpatterns = [
    path('v1/signup/', signup),
    path('v1/audiorecord/', AudiorecordCreate.as_view()),
    path('record/', download_record, name='record')
]
