from django.urls import path
from . import views

urlpatterns = [
    path('chatting', views.chatting, name='chatting')
]
