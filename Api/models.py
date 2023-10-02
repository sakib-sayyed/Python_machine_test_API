from django.db import models
from django.contrib.auth.models import User

class Clients(models.Model):
    client_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User,on_delete=models.CASCADE,related_name='created_client')
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.client_name

class Projects(models.Model):
    project_name = models.CharField(max_length=255)
    client = models.ForeignKey(Clients, on_delete=models.CASCADE, related_name='projects')
    users = models.ManyToManyField(User, related_name='projects')
    created_at = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE,related_name='created_project')

    def __str__(self):
        return f"{self.project_name} is Client {self.client}'s Project"