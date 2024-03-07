from . import views
from django.urls import path

urlpatterns = [
    path('', views.FoodOfferingList.as_view(), name='foodblog'),
    path('<slug:slug>/', views.food_offering_detail, name='food_offering_detail'),
]
