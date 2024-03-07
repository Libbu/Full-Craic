from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import Profile


# Create your views here.

class ProfileList(generic.ListView):
  
    queryset = Profile.objects.filter(status=1)
    template_name = "###"
    paginate_by = 6

def profile_detail(request, profile_id):
    profile = get_object_or_404(Profile, pk=profile_id)
    return render(request, 'profile_detail.html', {'profile': profile})