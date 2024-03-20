from django.shortcuts import render, redirect

from django.contrib import messages
from django.contrib.auth.forms import authenticate
from django.contrib.auth import login


def login_page(request):
    if request.user.is_authenticated:
        return redirect('main')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('main')
            else:
                messages.info(request, 'Username or password is incorrect')

        context = {}

        return render(request, 'login.html', context)


def logout(request):
    return render(request, 'logout.html')
