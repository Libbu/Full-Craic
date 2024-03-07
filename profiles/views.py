from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Profile


# Create your views here.

class ProfileList(generic.ListView):
  
    queryset = Profile.objects.filter(status=1)
    template_name = "wellnessblog/profiles.html"
    paginate_by = 6