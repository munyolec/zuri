from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, User

# Create your views here.
class BlogListView(ListView):
    model=Post
    template_name='home.html'
    
class BlogDetailView(DetailView):
    model=Post
    template_name='post_template.html'

class BlogCreateView(CreateView):
    model=Post
    template_name='post_new.html'
    fields=['title','author','body']

class BlogUpdateView(UpdateView):
    model=Post
    template_name="post_edit.html"
    fields=['title','body']

class BlogDeleteView(DeleteView):
    model=Post
    template_name="post_delete.html"
    success_url=reverse_lazy('home')

class UserRegisterView(CreateView):
    model=User
    template_name="register.html"
    fields=['first_name', 'last_name', 'email']
class UserListView(ListView):
    model=User
    template_name='user_list.html'

class UserDetailView(DetailView):
    model=User
    template_name='user.html'
