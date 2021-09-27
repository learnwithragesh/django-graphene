from django.db import models

# Create your models here.
class Todo(models.Model):
    content = models.TextField(blank=False)
    open = models.BooleanField(default=True)
    createdOn = models.DateTimeField(auto_now_add=True)