
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from .models import TODO

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username, password)
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/todo')
        else:
            return render(request, 'login.html', {'error': 'Invalid username or password'})
    return render(request, 'login.html')

def signup_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        # Check if username already exists
        if User.objects.filter(username=username).exists():
            return render(request, 'sign.html', {'error': 'Username already taken, choose another!'})

        User.objects.create_user(username=username, email=email, password=password)
        return redirect('/')

    return render(request, 'sign.html')

def todo_page(request):
    if request.method == "POST":
        title = request.POST.get('title')
        if title:
            TODO(title=title, user=request.user).save()
        return redirect('/todo')

    res = TODO.objects.filter(user=request.user).order_by('-date')
    total = res.count()
    completed = res.filter(is_completed=True).count()
    active = total - completed
    percent = int((completed / total * 100)) if total > 0 else 0

    return render(request, 'todo.html', {
        'res': res,
        'total': total,
        'completed': completed,
        'active': active,
        'percent': percent,
    })

def delete_todo(request, todo_id):
    TODO.objects.filter(id=todo_id, user=request.user).delete()
    return redirect('/todo')
def toggle_todo(request, todo_id):
    todo = TODO.objects.get(id=todo_id, user=request.user)
    todo.is_completed = not todo.is_completed
    todo.save()
    return redirect('/todo')

def logout_page(request):
    logout(request)
    return redirect('/')