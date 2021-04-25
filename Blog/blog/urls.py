from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView, UserRegisterView, UserListView, UserDetailView

urlpatterns =[
    path('users/',UserListView.as_view(),name='user_list'),
    path('user/new/',UserRegisterView.as_view(),name="register"),
    path('user/<int:pk>/',UserDetailView.as_view(),name='user'),


    path('post/<int:pk>/delete/',BlogDeleteView.as_view(), name="post_delete"),
    path('post/<int:pk>/edit/',BlogUpdateView.as_view(), name="post_edit"),
    path('post/new', BlogCreateView.as_view(), name='post_new'),
    path('post/<int:pk>/',BlogDetailView.as_view(),name='post_template'),
    path('',BlogListView.as_view(), name='home')
]

