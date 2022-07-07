from django.forms import ModelForm
from django import forms
from .models import Movie, Link

class UploadForm(ModelForm):
    name = forms.TextInput()
    image = forms.ImageField()
    class Meta:
        model = Movie
        fields = ['name', 'image']

class PostForm(ModelForm):
    class Meta:
        model = Link
        fields = '__all__'
        