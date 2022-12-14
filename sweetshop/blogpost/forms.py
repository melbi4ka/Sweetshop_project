from django import forms

from sweetshop.blogpost.models import BlogPost


class CreateBlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        exclude = ('date_created', )
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Blog post title'}),
            'text': forms.Textarea(attrs={'placeholder': 'Blog post text'}),
            'author': forms.TextInput(attrs={'value': '', 'id': 'author', 'type': 'hidden'}),
        }


class EditBlogPostForm(forms.ModelForm):
    class Meta:
        model = BlogPost
        exclude = ('date_created',)
        widgets = {
            'author': forms.TextInput(attrs={'value': '', 'id': 'author', 'type': 'hidden'}),
        }
