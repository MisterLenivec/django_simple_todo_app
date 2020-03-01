from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Task
from .forms import TaskForm


def index(request):
    tasks = Task.objects.all()
    form = TaskForm()

    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Задача успешно создана!')
        else:
            messages.warning(request, 'Задача не создана!')
        return redirect('/')

    context = {'tasks': tasks, 'form': form}

    return render(request, 'tasks/list.html', context)


def update_task(request, pk):
    task = Task.objects.get(id=pk)
    form = TaskForm(instance=task)

    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Задача успешно обновлена!')
        else:
            messages.warning(request, 'Задача не обновлена!')
        return redirect('/')

    context = {'form': form, 'task': task}

    return render(request, 'tasks/update_task.html', context)


def delete_task(request, pk):
    item = Task.objects.get(id=pk)

    if request.method == 'POST':
        item.delete()
        messages.success(request, 'Задача удалена!')
        return redirect('/')

    context = {'item': item}

    return render(request, 'tasks/delete_task.html', context)
