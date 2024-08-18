from django.conf import settings
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import os
from .serializers import FileCreateSerializer


FILE_PATH = os.path.join(settings.BASE_DIR, 'storage')
os.makedirs(FILE_PATH, exist_ok=True)

class ReadWriteFileView(APIView):

    def get(self, request):
        filename = request.query_params.get('filename')
        if not filename:
            return Response({'content': [], 'error': 'Please provide the filename.'}, status=status.HTTP_400_BAD_REQUEST)
        
        file_path = os.path.join(FILE_PATH, filename)
        if not os.path.exists(file_path):
            return Response({'content': [], 'error': 'File not found.'}, status=status.HTTP_400_BAD_REQUEST)
        
        try:
            with open(file_path, 'r') as file:
                content = file.read()
            return Response({'content': content}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'content': [], 'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    def post(self, request):
        try:
            serializer = FileCreateSerializer(data=request.data)
            if serializer.is_valid():
                filename = serializer.validated_data['filename']
                content = serializer.validated_data['content']

                file_path = os.path.join(FILE_PATH, filename)
                with open(file_path, 'w') as file:
                    file.write(content)
                return Response({'message': f"File '{filename}' created successfully."}, status=status.HTTP_201_CREATED)
            return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
