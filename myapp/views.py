from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import render


def index(request):
    title = 'Django Course'
    return render(request, 'index.html',{
        'title': title
    })

def hello(request, username):
    return HttpResponse("<h1>Hello %s<h1/>" %username)

def about(request):
    username = 'Flexo'
    return render(request,'about.html', {
        'username': username
    })

def projects(request):
    # projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request,'projects.html', {
        'projects': projects
    })


def task(request):
    # task = Task.objects.get(title=title)
    tasks = Task.objects.all()
    return render(request,'task.html',{
        'tasks': tasks
    })
