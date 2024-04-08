from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponse
from .models import Profile
from .forms import UserProfileForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# profiles = [
#     {'id':1, 'name':'Me'},
#     {'id':2, 'name':'Myself'},
#     {'id':3, 'name':'I'},
# ]


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try: 
            user = User.objects.get(username=username)
        except:
            messages.error(request, 'User doesnt exist')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('profiles')
        else:
            messages.error(request, 'Username or password doesnt exist')


    context = {}
    return render(request, 'base/login_register.html', context)

def logoutUser(request):
    logout(request)
    return redirect('home')


def home(request):
    return render(request, 'base/home.html')

def profiles_page(request):
    profiles = Profile.objects.all()
    context = {'profiles': profiles}
    return render(request, 'base/profiles.html', context)

def profile(request, pk):
    profile = Profile.objects.get(id=pk)
    context = {'profile': profile}
    return render(request, 'base/profile.html', context)

def profile_form(request):
    form = UserProfileForm()
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()

            return redirect('profiles')
    context = {'form': form}
    return render(request, 'base/profile-form.html', context)


def fill_form_prompt(request):
    return render(request, 'base/fill-form-prompt.html')

def edit_form(request, pk):
    profile = Profile.objects.get(id=pk)
    form = UserProfileForm(instance=profile)

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            return redirect('profiles')
    context = {'form': form}
    return render(request, 'base/profile-form.html', context)


def delete_profile(request, pk):
    profile = Profile.objects.get(id=pk)
    if request.method == 'POST':
        profile.delete()
        return redirect('profiles')
    return render(request, 'base/delete.html', {'obj':profile})
