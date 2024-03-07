from django.db import models
from django.contrib.auth.models import User
class Project(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology_used = models.CharField(max_length=255)
    image = models.ImageField(upload_to='project_images/')
    link = models.URLField(blank=True,null=True)

    def __str__(self):
        return self.title
