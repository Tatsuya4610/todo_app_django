import re
from django.db import models

class TodoModel(models.Model):
    title = models.CharField(max_length=20)
    memo = models.TextField()

    def __str__(self):
        return self.title