from django.db import models


# Create your models here.
class container(models.Model):
    name = models.CharField(max_length=50)
    image_name = models.CharField(max_length=50)
    time = models.DateTimeField()
    state = models.CharField(max_length=50)



class logs(models.Model):
    container = models.CharField(max_length=50)
    name = models.CharField(max_length=50)

    levelname = models.CharField(max_length=50)
    time = models.DateTimeField()

    message = models.TextField()
    error = models.TextField()


