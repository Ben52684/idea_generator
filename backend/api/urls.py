from django.urls import path
from .views import index, chat_response, HackathonIdeaList
from django.views.generic import TemplateView


urlpatterns = [
    
    path('', TemplateView.as_view(template_name="frontend/index.html"), name='index'),
    path('chat/', chat_response, name='chat_response'), 
    path('hackathon-ideas/', HackathonIdeaList.as_view(), name='hackathon-ideas-list'),

]