from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'author', 'content']

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Give a title'}),
            'slug': forms.TextInput(attrs={'class':'form-control'}),
            'author': forms.Select(attrs={'class':'form-control'}),
            'content': forms.Textarea(attrs={'class':'form-control'}),
        }


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Give a title'}),
            'content': forms.Textarea(attrs={'class':'form-control'}),
        }