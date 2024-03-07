from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

class Profile(models.Model):
    """
    Stores admin data for presentation.
    """
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_profile"
    )
    username = models.CharField(max_length=200, unique=True)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    image = CloudinaryField('image', default='placeholder')
    about = models.TextField()

    def __str__(self):
        return f"Admin:{self.username}"