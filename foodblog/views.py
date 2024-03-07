from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import Session, Comment, UserProfile
from .forms import CommentForm


# Create your views here.

class FoodSessionList(generic.ListView):
  
    queryset = FoodSession.objects.filter(status=1)
    template_name = "wellnessblog/index/foodblog.html"
    paginate_by = 6
    
def food_session_detail(request, slug):

    queryset = FoodSession.objects.filter(status=1)
    session = get_object_or_404(queryset, slug=slug)

    comments = session.comments.all().order_by("-created_on")
    comment_count = session.comments.filter(approved=True).count()

    #WORKING
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            # commment.user not comment.author
            comment.user = request.user
            comment.session = session
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )

    comment_form = CommentForm()    
   
    return render(request, "foodblog/food_session_detail.html", {'food_session': session, "comments": comments, "comment_count": comment_count, "comment_form": comment_form},)

def user_profile_detail(request, user_profile_id):
    user_profile = get_object_or_404(UserProfile, pk=user_profile_id)
    return render(request, 'user_profile_detail.html', {'user_profile': user_profile})

def create_food_session(request):
    if request.method == 'POST':
        form = FoodSessionForm(request.POST)
        if form.is_valid():
            session = form.save()
            return HttpResponseRedirect(reverse('session_detail', args=[session.id]))
    else:
        form = FoodSessionForm()
    return render(request, 'create_session.html', {'form': form})