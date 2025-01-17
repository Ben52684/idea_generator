from django.db import models

class Chat(models.Model):
    message = models.CharField(max_length=10000)
    response = models.CharField(max_length=10000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message

class HackathonIdea(models.Model):
    name = models.CharField(max_length=10000)
    description = models.CharField(max_length=10000)
    build_approach = models.CharField(max_length=10000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
