from django.shortcuts import render, redirect
from .models import Task
from django.shortcuts import get_object_or_404
from .forms import TaskForm  

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'todo/task_list.html', {'tasks': tasks})

def add_task(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        Task.objects.create(title=title, description=description)
        return redirect('task_list')
    return render(request, 'todo/add_task.html')

def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return redirect('task_list')

def toggle_task(request, task_id):
    if request.method == 'POST':
        task = get_object_or_404(Task, id=task_id)
        task.completed = not task.completed
        task.save()
        return redirect('task_list')

def edit_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    form = TaskForm(request.POST or None, instance=task)
    if form.is_valid():
        form.save()
        return redirect('task_list')
    return render(request, 'todo/edit_task.html', {'form': form})