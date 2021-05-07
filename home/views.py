import requests
from django.shortcuts import render, redirect


def home_view(request):
    context = {
        'title': 'Home'
    }
    return render(request, 'home/home.html', context)


def profile_view(request, username):
    context = {
        'title': username
    }

    if username is not None:
        user = requests.get("https://api.github.com/users/" + username).json()
        try:
            context['message'] = user['message']
        except:
            context['user'] = user



    else:
        return redirect('')

    return render(request, 'home/profile.html', context)
