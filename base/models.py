from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse



class Task(models.Model):
    title = models.CharField(blank=True,null=True,max_length=200)
    description = models.TextField(max_length=700)
    complete = models.BooleanField(default=False)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


    # ordering by complete
    class Meta:
        ordering = ['-complete']

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("task-list")
    
    def save(self, *args, **kwargs):
        return super().save(*args, **kwargs)
    
