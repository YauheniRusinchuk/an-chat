from django.urls import path
from .views import CreateRoom

app_name = 'room'

urlpatterns = [
    path('create/', CreateRoom.as_view(), name='create_new_room'),
]
