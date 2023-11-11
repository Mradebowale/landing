from django.db import models

# Create your models here.
class contact(models.Model):
    name = models.CharField(max_length=100)
    Message = models.TextField(max_length=10000)
    email = models.EmailField()


    def __str__(self):
        return self.name



