from django.db import models
from django.contrib.auth.models import User

class Ticket(models.Model):
    task=models.CharField(max_length=100)
    completed=models.BooleanField(default=False)
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.task
