from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from Todo_API.models import Todo
from Todo_API.serializers import TodoSerializer


class TodoEndpoints(APIView):
    def get(self, request):
        tasks = Todo.objects.all()
        serializer = TodoSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)