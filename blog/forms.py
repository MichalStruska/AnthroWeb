from django import forms
from .models import Post, Category
from django_extensions.db.fields import AutoSlugField
from django.template.defaultfilters import slugify

choices = Category.objects.all().values_list('name','name')

choice_list = []

for item in choices:
    choice_list.append(item)

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'author', 'category', 'content', 'snippet', 'thumbnail_image', 'article_image']

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control', 'placeholder':'give a title'}),
            #'slug': forms.TextInput(attrs={'class':'form-control'}),
            # 'slug': AutoSlugField(populate_from=['title']),
            # 'author': forms.Select(attrs={'class':'form-control'}),
            'author': forms.TextInput(attrs={'class':'form-control', 'value':'', 'id':'elder','type':'hidden'}),
            'category': forms.Select(choices=choice_list, attrs={'class':'form-control'}),
            'content': forms.Textarea(attrs={'class':'form-control'}),
            'snippet': forms.Textarea(attrs={'class':'form-control'}),
            
        }

        def save(self, *args, **kwargs):
            self.slug = slugify(self.title)
            super(Post, self).save(*args, **kwargs)


class EditForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'category', 'content', 'snippet']

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'category': forms.Select(choices=choice_list, attrs={'class':'form-control'}),
            'content': forms.Textarea(attrs={'class':'form-control'}),
            'snippet': forms.Textarea(attrs={'class':'form-control'}),
        }
