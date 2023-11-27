# todo/todo_api/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import ChannelProfile
from .serializer import ChannelProfileSerializer

class ProfileListApiView(APIView):
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        profiles = ChannelProfile.objects.all()
        serializer = ChannelProfileSerializer(profiles, many=True,context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

   