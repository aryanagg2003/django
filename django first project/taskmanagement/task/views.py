from django.shortcuts import render,redirect, get_object_or_404
from .forms import TaskForm
from .models import Task

def task_list(request):
    tasks = Task.objects.all()
    return render(request, "task_list.html", {'tasks': tasks})

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
# Create your views here.
