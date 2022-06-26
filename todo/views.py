from rest_framework import viewsets, status
from rest_framework.response import Response
from todo.models import Tasks
from todo.serializers import TaskSerializer


class TasksViewSet(viewsets.ViewSet):
    serializer_class = TaskSerializer

    def select(self, request):
        tasks = Tasks.objects.all().values('id', 'task_name', 'deadline', 'completed')
        serializer = TaskSerializer(tasks, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

    def detail(self, request, task_id: int):
        import pdb
        pdb.set_trace()
        task = Tasks.objects.filter(id=task_id).values('id', 'task_name', 'deadline', 'completed')
        serializer = TaskSerializer(task, many=True)
        return Response(status=status.HTTP_200_OK, data=serializer.data)

