import re
from django.db import models

# 'danger' = Bootstrapで用意されている色,'high'= データーで持っている。
CHOICE = (('danger','high'),('warning','normal'),('primary','low'))

class TodoModel(models.Model):
    title = models.CharField(max_length=20)
    memo = models.TextField()
    priority = models.CharField(
        max_length=50,
        choices = CHOICE
    )
    date = models.DateField()


    def __str__(self):
        return self.title