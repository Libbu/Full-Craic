from .models import FoodComment
from django import forms


class FoodCommentForm(forms.ModelForm):
    class Meta:
        model = FoodComment
        fields = ('comment_body',)