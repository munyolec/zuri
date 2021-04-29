from django.urls import path
from .import views
from django.contrib.auth.views import LoginView,LogoutView
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView, UserRegisterView, UserListView, UserDetailView

urlpatterns =[
    path('users/',UserListView.as_view(),name='user_list'),
    path('user/<int:pk>/',UserDetailView.as_view(),name='user'),
    path('register/', views.registerPage, name="register"),
    # path('logout/', LogoutView.as_view(), name='logout'),
    path('login/', LoginView.as_view(),name='login'),

    path('post/<int:pk>/delete/',BlogDeleteView.as_view(), name="post_delete"),
    path('post/<int:pk>/edit/',BlogUpdateView.as_view(), name="post_edit"),
    path('post/new', BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/',BlogDetailView.as_view(),name='post_template'),
    path('',BlogListView.as_view(), name='home')
]

