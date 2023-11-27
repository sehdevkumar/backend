from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from .models import Blog
from .serializer import BlogSerializer  # Correct the import statement for the serializer

class BlogView(APIView):
    def post(self, request, *args, **kwargs):
        print(request.data)
        payloads = {}
        payloads['user_id'] = int(request.data['user_id'])
        payloads['text'] = request.data['text']
        payloads['title'] = request.data['title']
        serializer = BlogSerializer(data=payloads)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
    def get(self, request, *args, **kwargs):
        '''
        List all the todo items for given requested user
        '''
        profiles = Blog.objects.all().order_by('-created_at')
        serializer = BlogSerializer(profiles, many=True,context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)


