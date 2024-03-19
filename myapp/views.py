from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import render, redirect
from .forms import CreateNewTask

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

def create_task(request):
    if request.method == 'GET':
        return render(request, 'create_task.html', {
            'form' : CreateNewTask()
        })
    else:
            Task.objects.create(title=request.POST['title'], description=request.POST['description'], project_id=2)
            return redirect('/task/')
  
    