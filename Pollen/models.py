from django.db import models

# Create your models here.
class Image(models.Model):
	photo = models.ImageField(upload_to = "myimage")

class Text(models.Model):
    city = models.CharField(max_length = 200)