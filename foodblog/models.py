from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

class FoodSession(models.Model):
    """
    Stores a single food event entry related to :model:`UserProfile`.
    """
    name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True)
    provider = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="sessions_provider"
    )
    image = CloudinaryField('image', default='placeholder')
    about = models.TextField(editable=True)
    location = models.CharField(max_length=200, blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)
    session_date_time = models.DateTimeField(blank=True, null=True)
    updated_on = models.DateTimeField(auto_now=True)
    participants = models.ManyToManyField(
        UserProfile, related_name='attended_sessions', blank=True
    )
    keywords = models.CharField(max_length=200, blank=True, null=True)
    status = models.IntegerField(choices=STATUS, default=0)
    
    class Meta:
        ordering = ["-session_date_time"]
        
    def __str__(self):
        return f"Session:{self.name} | provided by {self.provider}"


class Comment(models.Model):
    """
    Stores a comment and feedback from a user related to :model:`UserProfile`
    regarding a food event related to :model:`Session`.
    """
    session = models.ForeignKey(
        Session, on_delete=models.CASCADE, related_name="comments"
    )
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="user_comment"
    )
    created_on = models.DateTimeField(auto_now_add=True)
    comment_body = models.TextField()
    approved = models.BooleanField(default=False)
    stars = models.IntegerField(choices=[(i, i) for i in range(1, 12)],blank=True, null=True)  # Restrict to values 1 to 11 = 0 - 5 stars in half-star increments

    class Meta:
        ordering = ["-created_on"]
        
    def __str__(self):
        return f"Comment by {self.user} on {self.session}"
