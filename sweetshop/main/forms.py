from django import forms

from sweetshop.main.models import SubscribedUser


class NewsSubscriptCreateForm(forms.ModelForm):
    class Meta:
        model = SubscribedUser
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Fill your name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Fill your email'}),
        }


class SearchForm(forms.Form):
    search_name = forms.CharField(
        max_length=30,
    )
