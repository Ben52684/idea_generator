from django.views.generic import TemplateView
from django.urls import path, include
from django.contrib import admin

urlpatterns = [
    path('', TemplateView.as_view(template_name="frontend/index.html"), name='index'),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    
]
