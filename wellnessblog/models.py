from django.contrib.auth.models import User
from django.db import models
from cloudinary.models import CloudinaryField

class UserProfile(models.Model):
    """
    Stores user data related to :model:`auth.User`.
    """
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_profile"
    )
    STUDENT = "STU"
    THERAPIST = "THE"
    INSTRUCTOR = "INS"
    FOOD_VENDOR = "FOO"
    ROLE_CHOICES = (
        (STUDENT, "Student"),
        (THERAPIST, "Therapist"),
        (INSTRUCTOR, "Instructor"),
        (FOOD_VENDOR, "Food Vendor"),
    )
    user_role = models.CharField(max_length=300, choices=ROLE_CHOICES)
    username = models.CharField(max_length=200, unique=True)
    firstname = models.CharField(max_length=200)
    lastname = models.CharField(max_length=200)
    image = CloudinaryField('image', default='placeholder')
    sessions_attended = models.ManyToManyField(
        'Session', related_name='attendees'
    )

    def __str__(self):
        return f"User:{self.username}"


class Session(models.Model):
    """
    Stores a single session entry related to :model:`auth.UserProfile`.
    """
    name = models.CharField(max_length=200, unique=True)
    provider = models.ForeignKey(
        UserProfile, on_delete=models.CASCADE, related_name="sessions_provided"
    )
    image = CloudinaryField('image', default='placeholder')
    about = models.TextField()
    location = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)
    session_date_time = models.DateTimeField(blank=True)
    updated_on = models.DateTimeField(auto_now=True)
    max_participants = models.IntegerField()
    participants = models.ManyToManyField(
        UserProfile, related_name='attended_sessions'
    )
    keywords = models.CharField(max_length=200)
    
    class Meta:
        ordering = ["-session_date_time"]
        
    def __str__(self):
        return f"Session:{self.name} | provided by {self.provider}"
