from django.urls import path
from .views import (home, about, contact, dashboard,user_signup, user_login, user_logout, add_post, update_post, delete_post, user_detail)

urlpatterns = [
    path('', home, name="home"), # blogs home page 
    path('about/', about, name="about"), # about page
    path('contact/', contact, name="contact"), # contact page
    path('dashboard/', dashboard, name="dashboard"),# dashboard (only access when logged in) 
    path('signup/', user_signup, name="signup"), # signup
    path('login/', user_login, name="login"), # login
    path('logout/', user_logout, name="logout"), # logout
    path('addpost/', add_post, name="addpost"), # add new blog (only access when logged in) 
    path('updatepost/<int:id>/', update_post, name="updatepost"), # update existing blog (only access when logged in) 
    path('deletepost/<int:id>/', delete_post, name="deletepost"), # delete existing blog (only access when logged in) 
    path('userdetail/', user_detail, name="userdetail"), # logged in user details (only access when logged in)
]
