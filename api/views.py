from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime
from rest_framework import generics

from .models import Room
from .serializers import RoomSerializer
