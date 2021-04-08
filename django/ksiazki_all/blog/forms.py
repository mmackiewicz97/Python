from django import forms
from .models import Post

class PostForm(forms.Form):
    title = forms.CharField(label='Tytul', max_length=200, required=True)
    slug = forms.CharField(label='Slug', max_length=200, required=True)
    author = forms.CharField(label='Author', max_length=200, required=True)
    updated_on = forms.DateTimeField()
    content = forms.CharField(label="Content", max_length=2000)
    created_on = forms.DateTimeField()
    status = forms.IntegerField()
