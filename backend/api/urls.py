from django.urls import path
from .views import index, chat_response, HackathonIdeaList


urlpatterns = [
    path('', index, name='index'),
    path('chat/', chat_response, name='chat_response'), 
    path('hackathon-ideas/', HackathonIdeaList.as_view(), name='hackathon-ideas-list'),

]