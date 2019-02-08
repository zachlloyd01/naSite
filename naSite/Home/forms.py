from django import forms
from .models import comment_page, password_reset, news_application
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.db import models
from tinymce.widgets import TinyMCE

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user

class CommentForm(forms.ModelForm):
    class Meta:
        model = comment_page
        fields = ('comment',)

class PasswordForm(forms.ModelForm):
    class Meta:
        model = password_reset
        fields = ("username", "password")

class NewsApp(forms.ModelForm):
    class Meta:
        model = news_application
        fields = ("name","reason",)