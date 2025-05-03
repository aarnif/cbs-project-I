from django.shortcuts import render, redirect
from django.db import connection
from users.models import User

# Create your views here.


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm-password')

        # FLAW 1: Injection (SQL Injection)
        cursor = connection.cursor()
        cursor.execute(f"SELECT * FROM users_user WHERE username = '{username}'")
        user_exists = cursor.fetchone()

        if user_exists:
            username = user_exists[1]
            return render(request, 'registration/register.html', {'error_message': f'Username {username} already exists'})

        # FLAW 1 FIX
        # try:
        #     user_exists = User.objects.get(username=username)
        #     return render(request, 'registration/register.html', {'error_message': f'Username {user_exists.username} already exists'})
        # except User.DoesNotExist:
        #     pass

        if password != confirm_password:
            return render(request, 'registration/register.html', {'error_message': 'Passwords do not match'})
        
        user = User.objects.create(username=username, password=password)
        user.save()

        request.session['user_id'] = user.id
        request.session['username'] = user.username
        
        return redirect('/polls/')
    
    return render(request, 'registration/register.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = User.objects.get(username=username)
        except User.DoesNotExist:
            return render(request, 'registration/login.html', {'error_message': "Invalid username or password"})

        check_password = User.objects.get(username=username).check_password(password)
        if not check_password:
            return render(request, 'registration/login.html', {'error_message': "Invalid username or password"})
        
        request.session['user_id'] = user.id
        request.session['username'] = user.username
        
        return redirect('/polls/')
        

    return render(request, 'registration/login.html')

def logout(request):
    request.session.flush()
    return redirect('/login/')
