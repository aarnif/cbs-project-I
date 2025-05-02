from django.shortcuts import render
from django.db import connection

# Create your views here.


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # FLAW 1: Injection
        # cursor = connection.cursor()
        # cursor.execute(f"SELECT * FROM users_user WHERE username = '{username}'")
        # user_exists = cursor.fetchone()

        # if user_exists:
        #     username = user_exists[1]
        #     return render(request, 'registration/register.html', {'error_message': f'Username {username} already exists'})

        # FIX
        from .models import User
        try:
            user_exists = User.objects.get(username=username)
            return render(request, 'registration/register.html', {'error_message': f'Username {user_exists.username} already exists'})
        except User.DoesNotExist:
            pass

        if password != confirm_password:
            return render(request, 'registration/register.html', {'error_message': 'Passwords do not match'})
 
    return render(request, 'registration/register.html')