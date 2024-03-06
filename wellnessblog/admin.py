from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin
from .models import Session, UserProfile, Comment

# Register your models here.

@admin.register(Session)
class SessionsAdmin(SummernoteModelAdmin):
    list_display = ('name', 'slug', 'status', 'created_on')
    search_fields = ['name', 'about']
    list_filter = ('status', 'created_on',)
    prepopulated_fields = {'slug': ('name',)}
    summernote_fields = ('about',)


admin.site.register(UserProfile)
admin.site.register(Comment)
