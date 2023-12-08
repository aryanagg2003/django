from django.shortcuts import render,redirect, get_object_or_404
from .forms import TaskForm
from .models import Task
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required 
from django.db.models import Q
from django.utils import timezone
from datetime import timedelta


def task_list(request):
    search_query = request.GET.get('search', '')
    filter_date = request.GET.get('filter_date', '')

    tasks = Task.objects.filter(Q(title__icontains=search_query) | Q(description__icontains=search_query))

    if filter_date == 'today':
        tasks = tasks.filter(created_at__date=timezone.now().date())
    elif filter_date == 'week':
        tasks = tasks.filter(created_at__date__gte=timezone.now().date() - timedelta(days=7))

    return render(request, "task_list.html", {'tasks': tasks, 'search_query':search_query, 'filter_date': filter_date})


def task_detail(request, pk):
    task = get_object_or_404(Task, pk=pk)
    return render(request, "task_detail.html", {'task': task})


def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('task-list')  
    else:
        form = TaskForm()
    
    return render(request, 'task_create.html', {'form': form})


def task_update(request, pk):
    task = get_object_or_404(Task, pk=pk)  
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('task-list')
    else:
        form = TaskForm(instance=task)  
    return render(request, 'task_update.html', {'form': form, 'task': task})


def task_delete(request, pk):
    task = get_object_or_404(Task, pk=pk)
    if request.method == "POST":  
        task.delete()
        return redirect('task-list')
    return render(request,'task_delete.html',{'task':task})

def login_page(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is None:
            messages.error(request, 'Invalid credentials')
            return render(request, 'login.html')

        login(request, user)
        return redirect('task-list')

    return render(request, 'login.html')

def logout_page(request):
    logout(request)
    return redirect('login-page')

def register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already taken')
            return redirect('register')

        user = User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password
        )

        messages.info(request, 'Account created successfully')
        return redirect('login-page')

    return render(request, 'register.html')
# Create your views here.
