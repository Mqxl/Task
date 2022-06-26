from rest_framework import serializers

from todo.models import Tasks


class TaskSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tasks
        fields = ('id', 'task_name', 'deadline', 'completed')
