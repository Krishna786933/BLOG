from django.db import models
from django.contrib.auth.models import User

class PostModel(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    dete_created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-dete_created',)

    def __str__(self):
        return self.title



# Create your models here.
