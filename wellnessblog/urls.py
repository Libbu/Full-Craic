from . import views
from django.urls import path

urlpatterns = [
    path('', views.SessionList.as_view(), name='home'),
    path('<slug:slug>/', views.session_detail, name='session_detail'),
    path('<slug:slug>/edit_comment/<int:comment_id>', views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>', views.comment_delete, name='comment_delete'),
    path('update_rating/', views.update_rating, name='update_rating'),
]