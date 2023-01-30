

from django.urls import path, include

from django.contrib import admin

from miniotest.views.home import Home
from miniotest.views.signed_url import SignedUrlView
from miniotest.views.upload import FileUploadView

urlpatterns = [
    path('', Home.as_view()),
    path('upload', FileUploadView.as_view()),
    path('surl', SignedUrlView.as_view())


]


