from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('get_transcript/', views.get_transcript_long, name='get_transcript_long'),
]
