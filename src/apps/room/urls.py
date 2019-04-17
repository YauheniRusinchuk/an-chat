from django.urls import path
from .views import CreateRoom, DetailtRoom

app_name = 'room'

urlpatterns = [
    path('<slug:slug>/id<int:pk>/', DetailtRoom.as_view(), name='detail_room'),
    path('create/', CreateRoom.as_view(), name='create_new_room'),
]
