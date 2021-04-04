from django.urls import path
from .views import *
urlpatterns = [

    path('home', home,name='home'),
    path('signup', user_signup,name='signup'),
    path('login', user_login,name='login'),
    path('logout', user_logout,name='logout'),
    path('', posts,name='posts'),
    path('create_post', create_post,name='create_post'),
    path('about_me', about_me,name='about_me'),
    path('add_comment/<int:pk>',add_comment,name='add_comment'),
    path('add_reply/<int:pk>',add_reply,name='add_reply'),
    path('like_post/<int:pk>',like_post,name='like_post'),
    path('post/<str:pk>', detail,name='post_detail')
    # path('post_detail/<int:pk>',DetailView.as_view(),name='post_detail')
]
