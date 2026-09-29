from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from Todo_API.models import Todo
from rest_framework.permissions import IsAuthenticated
from Todo_API.serializers import TodoSerializer

class TodoEndpoints(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        tasks = Todo.objects.filter(user=request.user)
        serializer = TodoSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateingPoints(APIView):
    permission_classes = [IsAuthenticated]

    def put(self, request, pk):
        task = get_object_or_404(Todo, pk=pk, user=request.user)
        serializer = TodoSerializer(task, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, pk):
        task = get_object_or_404(Todo, pk=pk, user=request.user)
        serializer = TodoSerializer(task, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk):
        task = get_object_or_404(Todo, pk=pk, user=request.user)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)