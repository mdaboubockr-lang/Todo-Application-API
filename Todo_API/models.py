from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):

    CHOICES_STATUS = [
        ('Pending', 'Pending'),
        ('completed', 'Completed'),
        ('incomplete', 'Incomplete'),
    ]

    task_summary = models.CharField(max_length=255)
    task_detail = models.TextField()
    task_deadline = models.DateTimeField()
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name='todos')
    task_status = models.CharField(choices=CHOICES_STATUS, default='Pending')