from django.urls import path
from .views import ReadWriteFileView


urlpatterns = [
    path('file/', ReadWriteFileView.as_view(), name='file'),
]