from django.urls import path
from .views import index, chatbot

urlpatterns = [
    path('', index, name='index'),
    path('orion/', chatbot, name='chatbot')
]