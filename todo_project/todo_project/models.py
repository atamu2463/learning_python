from django.db import models

# Todoに入れるデータを定義

class TodoTask(models.Model):
    title = models.CharField(max_length=200)
    completed = models.BooleanField(default=False)
    description = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.title