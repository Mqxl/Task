from datetime import datetime

from django.db import models

# Create your models here.


class Tasks(models.Model):
    id = models.AutoField(primary_key=True)
    task_name = models.CharField(max_length=100)
    task_description = models.TextField()
    deadline = models.DateTimeField(default=datetime.now())
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.task_name

