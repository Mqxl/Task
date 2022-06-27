from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.contrib.sessions.models import Session
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from todoapp.settings import EMAIL_HOST_PASSWORD
from todo.models import Tasks
from todo.serializers import TaskSerializer, CreateTaskSerializer, CompleteTaskSerializer
from todo.tasks import my_task


class TasksViewSet(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CreateTaskSerializer

    def get(self, request):
        tasks = Tasks.objects.all().values('id', 'task_name', 'deadline', 'completed')
        serializer = TaskSerializer(tasks, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def post(self, request):
        serializer = CreateTaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TasksDetailViewSet(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TaskSerializer

    def get(self, request, pk: int):
        task = Tasks.objects.filter(id=pk).values('id', 'task_name', 'deadline', 'completed')
        serializer = TaskSerializer(task, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def put(self, request, pk: int):
        task = Tasks.objects.get(id=pk)
        serializer = TaskSerializer(task, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=201, data=serializer.data)
        return Response(status=400, data="wrong parameters")

    def delete(self, request, pk: int):
        task = Tasks.objects.get(id=pk)
        task.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class TaskCompleteViewSet(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class = CompleteTaskSerializer

    def post(self, request, pk: int):
        task = Tasks.objects.get(id=pk)
        task.completed = True
        task.save()
        serializer = TaskSerializer(task)
        if len(EMAIL_HOST_PASSWORD) > 0:
            my_task(10, 'Subject Example', 'Example message', 'example@gmail.com')
        return Response(status=201, data=serializer.data)


class Logout(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        logout(request)
        return Response('User Logged out successfully')


