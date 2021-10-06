from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import Group, User
from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages
from .models import Contact, Post
from .forms import LoginForm, PostForm, SignupForm, ContactForm, EditUserDetailForm


# Blogs Homepage
def home(request):
    posts = Post.objects.all()
    context = {'posts':posts}
    return render(request, 'home.html', context) 

# About Page
def about(request):
    return render(request, 'about.html') 

# Contact Page
def contact(request):
    if request.method == 'POST':
        fm = ContactForm(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            add = fm.cleaned_data['address']
            msg = fm.cleaned_data['message']
            reg = Contact(name=nm, email=em, address=add, message=msg)
            reg.save()
            messages.success(request, "Message Sent Successfully!")
            # fm = ContactForm()
    else:
        fm = ContactForm()
    context = {'form':fm}
    return render(request, 'contact.html', context) 

# Dasboard (only access when user is login)
def dashboard(request):
    if request.user.is_authenticated:
        posts= Post.objects.all()
        user = request.user
        full_name = user.get_full_name()
        grps = user.groups.all()
        context = {'posts':posts, 'full_name':full_name, 'groups':grps} 
        return render(request, 'dashboard.html', context)
    else:
        return HttpResponseRedirect('/login/') 

# SignUp View
def user_signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            fm = SignupForm(request.POST)
            if fm.is_valid():
                user = fm.save()
                messages.success(request, "Congratulations! You Have Become An Author! Please Login! ")

                # Adding user to Author group automatically
                group = Group.objects.get(name="Author")
                user.groups.add(group)

                return HttpResponseRedirect('/login/')
        else:
            fm = SignupForm()
        context = {'form':fm}
        return render(request, 'signup.html', context) 
    else:
        return HttpResponseRedirect('/dashboard/')

# Login View
def user_login(request):
    if not request.user.is_authenticated:
        if request.method=='POST':
            fm = LoginForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, "Logged In Successfully!")
                    return HttpResponseRedirect('/dashboard/')
        else:
            fm = LoginForm(request=request)
        context = {'form':fm}
        return render(request, 'login.html', context) 
    else:
        return HttpResponseRedirect('/dashboard/')

# Logout View
def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

# Adding new blog (only access when user is login)
def add_post(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            fm = PostForm(request.POST)
            if fm.is_valid():
                tle = fm.cleaned_data['title']
                desc = fm.cleaned_data['description']
                pst = Post(title=tle, description=desc)
                pst.save()
                messages.success(request, "Blog Created Successfully!")
                return HttpResponseRedirect('/dashboard/')
        else:
            fm = PostForm()
        context = {'form':fm}
        return render(request, 'addpost.html', context)
    else:
        return HttpResponseRedirect('/login/')

# Updating existing blog (only access when user is login)
def update_post(request, id):
    if request.user.is_authenticated:
        if request.method=='POST':
            pi = Post.objects.get(pk=id)
            fm = PostForm(request.POST, instance=pi)
            if fm.is_valid():
                fm.save()
                messages.success(request, "Blog Updated Successfully!")
                return HttpResponseRedirect('/dashboard/')
        else:
            pi = Post.objects.get(pk=id)
            fm = PostForm(instance=pi)
        context = {'form':fm}
        return render(request, 'updatepost.html', context)
    else:
        return HttpResponseRedirect('/login/')

# Deleting existing blog (only access when user is login & only ADMIN can delete blog)
def delete_post(request, id):
    if request.user.is_authenticated:
        if request.method=='POST':
            pi = Post.objects.get(pk=id)
            pi.delete()
            return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')

# View logged in user details (only access when user is login)
def user_detail(request):
    if request.user.is_authenticated:
        if request.method=='POST':
            fm = EditUserDetailForm(request.POST, instance=request.user)
            if fm.is_valid():
                fm.save()
                messages.success(request, "Profile Updated Successfully!")
                return HttpResponseRedirect('/dashboard/')
        else:
            fm = EditUserDetailForm(instance=request.user)
 
        return render(request, 'userdetail.html', {'form':fm})
    else:
        return HttpResponseRedirect('/login/')