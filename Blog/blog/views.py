from django.shortcuts import render, redirect, HttpResponseRedirect,HttpResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post, User
from django.views import generic
from django.contrib import messages
from .forms import CreateUserForm

from django.contrib.auth import authenticate, login, logout


from django.contrib.auth.forms import UserCreationForm

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
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'register.html'

    
class UserListView(ListView):
    model=User
    template_name='user_list.html'

class UserDetailView(DetailView):
    model=User
    template_name='user.html'


def registerPage(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=UserCreationForm
    return render(request, 'registration/register.html', {'form': form})




  