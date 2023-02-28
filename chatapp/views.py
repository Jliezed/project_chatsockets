from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.conf import settings
from user.forms import SignupForm
from .forms import RoomsForm


def signup_page(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-login user
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    else:
        form = SignupForm()
    return render(request, 'authentication/signup.html', context={'form': form})


def rooms(request):
    if request.method == 'POST':
        form = RoomsForm(request.POST)
        if form.is_valid():
            # DO SOMETHING
            room = form.cleaned_data['room_name']
            return redirect('chatapp:room', room_name=room)
    else:
        form = RoomsForm()

    context = {
        "form": form,
    }
    return render(request, 'rooms.html', context=context)


def room(request, room_name):
    user = request.user
    context = {
        'room_name': room_name,
        'username': user.username,
    }
    return render(request, 'room.html', context=context)
