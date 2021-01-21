from django.shortcuts import render, redirect
from django.http import HttpResponse
from TodoApp.models import Task
from TodoApp.forms import TaskForm
# Create your views here.


def demo(request):
    return HttpResponse("Iam Working Fine ..........)")


def home(request):
    tasks = Task.objects.all()
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request, 'TodoApp/home.html', {'form': form, 'tasks': tasks})


def create(request):
    form = TaskForm()
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    return render(request, 'TodoApp/create.html', {'form': form})


def update(request, id):
    task = Task.objects.get(id=id)
    form = TaskForm(instance=task)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')
    return render(request, 'TodoApp/update.html', {'form': form})


def delete(request, id):
    item = Task.objects.get(id=id)
    if request.method == 'POST':
        item.delete()
        return redirect('/')
    return render(request, 'TodoApp/delete.html', {'item': item})
