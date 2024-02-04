from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, 'Login successful!')
            return redirect('index')  
        else:
            messages.error(request, 'Invalid login credentials, Please try again.')

    return render(request, 'authentication\login.html')


def logout_user(request):
    if request.user.is_authenticated:
        logout(request)
        messages.warning(request, "You Have Been Logged Out...")
    return redirect('login')
