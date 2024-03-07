from . import views
from django.urls import path


urlpatterns = [
    path('', views.ProfileList.as_view(), name='profiles'),
    path('<slug:slug>/', views.profile_detail, name='profile_detail'),
]   