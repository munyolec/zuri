from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from django.contrib.auth.models import User
from django import forms


class CreateUserForm(UserCreationForm):
    email=forms.EmailField(required=True, label='Email',error_messages={'exists' : 'This already exists'})

    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']

    def save(self,commit=True):
        user=super(UserCreationForm,self).save(commit=False)
        user.email=self.cleaned_data['email']
        if commit:
            user.save()
    def clean_email(self):
        if User.objects.filter(email=self.cleaned_data['email']).exists():
            raise forms.ValidationError(self.fields['email'].error_messages['exists'])
        return self.cleaned_data['email']

