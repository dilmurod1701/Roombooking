from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from rest_framework import generics

from .models import Room
from .serializers import RoomSerializer


class AllRooms(generics.ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class RoomBooking(APIView):
    def post(self, request, room_id):
        try:
            room = Room.objects.get(id=room_id)
        except Room.DoesNotExist:
            return Response({"message": "Xona topilmadi yoki mavjud emas xona raqami kiritildi!"},
                            status=status.HTTP_404_NOT_FOUND)

        if room.booked:
            return Response({
                "message": "Xona allaqachon boshqa bir mijoz tomonidan band qilingan!",
                "available_from": room.end.strftime("%Y-%m-%d %H:%M:%S")
            }, status=status.HTTP_409_CONFLICT)

        room.booked = True
        room.start = datetime.now()
        room.end = room.start
        room.save()

        return Response({
            "message": "Xona allaqachon boshqa bir mijoz tomonidan band qilingan!",
            "room": room.name,
            "start": room.start.strftime("%Y-%m-%d %H:%M:%S"),
            "end": room.end.strftime("%Y-%m-%d %H:%M:%S")
        }, status=status.HTTP_201_CREATED)


def migration(request):
    import os
    os.system('python3 manage.py makemigrations')
    os.system('python3 manage.py migrate --no-input')
    return HttpResponse('Migration Done')