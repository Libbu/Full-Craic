from django.contrib import admin
from .models import FoodOffering, FoodComment
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.

@admin.register(FoodOffering)
class FoodOfferingAdmin(SummernoteModelAdmin):

    list_display = ('name', 'slug', 'status', 'created_on')
    search_fields = ['name']
    list_filter = ('status',)
    prepopulated_fields = {'slug': ('name',)}
    summernote_fields = ('about',)

admin.site.register(FoodComment)