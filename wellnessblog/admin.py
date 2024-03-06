from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Session, UserProfile, Comment

# Register your models here.

@admin.register(Session)
class SessionAdmin(SummernoteModelAdmin):

    list_display = ('name', 'slug', 'status', 'created_on')
    search_fields = ['name']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('name',)}
    summernote_fields = ('about',)

admin.site.register(UserProfile)
admin.site.register(Comment)
