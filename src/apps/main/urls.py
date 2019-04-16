from django.urls import path
from django.views.generic.base import TemplateView
from .views import index


app_name = 'main'

urlpatterns = [
    # path('', index, name='main_page'),
    path('', TemplateView.as_view(template_name='main/index.html'), name='main_page'),
]
