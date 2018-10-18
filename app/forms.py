from django import forms
from .models import *

# class CommentForm(forms.ModelForm):

#     class Meta:
#         model = Comment
#         exclude = ['poster', 'imagecommented']

class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']

class AddHoodForm(forms.ModelForm):
    class Meta:
        model = Neighborhood
        exclude = ['user_profile', 'profile']

