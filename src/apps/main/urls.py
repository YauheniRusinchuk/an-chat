from django.urls import path
from django.views.generic.base import TemplateView



app_name = 'main'

urlpatterns = [
    path('', TemplateView.as_view(template_name='main/index.html'), name='main_page'),
]
