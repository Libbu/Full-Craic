from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import FoodOffering, FoodComment
from .forms import FoodCommentForm


# Create your views here.

class FoodOfferingList(generic.ListView):
  
    queryset = FoodOffering.objects.filter(status=1)
    template_name = "foodblog/landingpage.html"
    paginate_by = 6
    
def food_offering_detail(request, slug):

    queryset = FoodOffering.objects.filter(status=1)
    food_offering = get_object_or_404(queryset, slug=slug)

    comments = food_offering.food_comments.all().order_by("-created_on")
    comment_count = food_offering.food_comments.filter(approved=True).count()

    #not WORKING
    if request.method == "POST":
        comment_form = FoodCommentForm(data=request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.user = request.user
            comment.food_offering = food_offering
            comment.save()
            messages.add_message(
                request, messages.SUCCESS,
                'Comment submitted and awaiting approval'
            )

    comment_form = FoodCommentForm()    
   
    return render(request, "foodblog/food_offering_detail.html", {'food_offering': food_offering, "comments": comments, "comment_count": comment_count, "comment_form": comment_form},)

def user_profile_detail(request, user_profile_id):
    user_profile = get_object_or_404(UserProfile, pk=user_profile_id)
    return render(request, 'user_profile_detail.html', {'user_profile': user_profile})

def create_food_session(request):
    if request.method == 'POST':
        form = FoodOfferingForm(request.POST)
        if form.is_valid():
            session = form.save()
            return HttpResponseRedirect(reverse('session_detail', args=[session.id]))
    else:
        form = FoodOfferingForm()
    return render(request, 'create_session.html', {'form': form})