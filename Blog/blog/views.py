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
        form = CreateUserForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            # new_user = authenticate(
            #     username=form.cleaned_data['username'],
            #     password=form.cleaned_data['password1']
            # )
            login(request, new_user,backend='django.contrib.auth.backends.ModelBackend')
            return redirect('home')
    else:
        form = CreateUserForm()
    return render(request, 'register.html', {'form': form})

# def loginPage(request):
# 	if request.user.is_authenticated:
# 		return redirect('home')
# 	else:
# 		if request.method == 'POST':
# 			username = request.POST.get('username')
# 			password =request.POST.get('password')

# 			user = authenticate(request, username=username, password=password)

# 			if user is not None:
# 				login(request, user)
# 				return redirect('home')
# 			else:
# 				messages.info(request, 'Username OR password is incorrect')

# 		context = {}
# 		return render(request, 'login.html', context)

class UserLoginView(CreateView):
    model=User
    success_url = reverse_lazy('home')
    template_name = 'login.html'
    fields=['username','password']


  