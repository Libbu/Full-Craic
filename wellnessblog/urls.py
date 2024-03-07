from . import views
from django.urls import path

urlpatterns = [
    path('', views.SessionList.as_view(), name='home'),
    path('<slug:slug>/', views.session_detail, name='session_detail'),
    path('update_rating/', views.update_rating, name='update_rating'),
]