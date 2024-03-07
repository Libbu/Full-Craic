from django.contrib import admin
from .models import Profile
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(Profile)
class ProfileAdmin(SummernoteModelAdmin):

    list_display = ('name', 'slug', 'status',)
    search_fields = ['name']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('name',)}
    summernote_fields = ('about',)