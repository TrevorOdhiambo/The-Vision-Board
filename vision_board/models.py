from django.db import models
from django.contrib.auth import get_user_model

class Vision(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField()
    author = models.ForeignKey(get_user_model(),on_delete=models.CASCADE,)

    def _str__(self):
        return self.title
    

class Goal(models.Model):
    vision = models.ForeignKey(Vision, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    due_date = models.DateField()

    def __str__(self):
        return self.title

class Intention(models.Model):
    goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    date_created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.title
