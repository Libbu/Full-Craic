from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length = 100)
    image = CloudinaryField('image', default = 'placeholder')
