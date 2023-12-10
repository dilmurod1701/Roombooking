from django.urls import path

from . import views


urlpatterns = [
    path('rooms', views.AllRooms.as_view(), name='room-list'),
    path('book/<int:room_name>', views.RoomBooking.as_view(), name='room-booking'),
    path('migration/', views.migration, name='migration'),
]
