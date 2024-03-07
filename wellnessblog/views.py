from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.urls import reverse
from .models import Session, Comment, UserProfile
from .forms import CommentForm


# Create your views here.

class SessionList(generic.ListView):
  
    queryset = Session.objects.filter(status=1)
    template_name = "wellnessblog/index.html"
    paginate_by = 6
    
def session_detail(request, slug):

    queryset = Session.objects.filter(status=1)
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
   
    return render(request, "wellnessblog/session_detail.html", {'session': session, "comments": comments, "comment_count": comment_count, "comment_form": comment_form},)

def user_profile_detail(request, user_profile_id):
    user_profile = get_object_or_404(UserProfile, pk=user_profile_id)
    return render(request, 'user_profile_detail.html', {'user_profile': user_profile})

def create_user_profile(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            user_profile = form.save()
            return HttpResponseRedirect(reverse('user_profile_detail', args=[user_profile.id]))
    else:
        form = UserProfileForm()
    return render(request, 'create_user_profile.html', {'form': form})

def create_session(request):
    if request.method == 'POST':
        form = SessionForm(request.POST)
        if form.is_valid():
            session = form.save()
            return HttpResponseRedirect(reverse('session_detail', args=[session.id]))
    else:
        form = SessionForm()
    return render(request, 'create_session.html', {'form': form})

# @csrf_exempt  # For simplicity, you can remove this decorator if you're using CSRF protection
def update_rating(request):
    if request.method == 'POST' and request.is_ajax():
        rating = request.POST.get('rating')  # Assuming rating is sent as POST data
        comment_id = request.POST.get('comment_id')  # Assuming you also send comment_id to identify the comment
        
        try:
            comment = Comment.objects.get(pk=comment_id)
            comment.stars = rating
            comment.save()
            return JsonResponse({'message': 'Rating updated successfully'})
        except Comment.DoesNotExist:
            return JsonResponse({'error': 'Comment not found'}, status=404)
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)