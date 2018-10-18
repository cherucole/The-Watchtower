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

# class UploadForm(forms.ModelForm):
#     class Meta:
#         model = Post
#         exclude = ['user_profile', 'profile','likes', 'opinions']

