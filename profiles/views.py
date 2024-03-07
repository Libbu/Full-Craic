from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Profile


# Create your views here.

class ProfileList(generic.ListView):
  
    queryset = Profile.objects.filter(status=1)
    template_name = "profiles/profiles_landingpage.html"
    paginate_by = 6

def profile_detail(request, firstname):
    profile = get_object_or_404(Profile, firstname=firstname)
    return render(request, 'profile_detail.html', {'profile': profile})