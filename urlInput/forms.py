from tkinter import Widget
from django.forms import ModelForm, Textarea
from django import forms
from .models import Movie, Link

class UploadForm(ModelForm):
    name = forms.TextInput()
    image = forms.ImageField()  
    class Meta:
        model = Movie
        fields = ['name', 'image']

# class PostForm(forms.ModelForm):
#     link_text = forms.CharField(required=False)
#     link_status_code = forms.CharField(required=False)
#     class Meta:
#         model = Link
#         fields = ['link_text', 'link_status_code']
#         widgets = {'link_text':forms.TextInput(attrs={'class':'form-control'}),
#                 'link_status_code':forms.TextInput(attrs={'class':'form-control'}),
#                 }
                
        
        