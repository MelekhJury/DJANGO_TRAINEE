from django.shortcuts import render, redirect
from .models import Task
from .forms import TaskForm
from django.http import HttpResponse
# Create your views here.


def index(request):
    tasks = Task.objects.order_by('id')
    return render(request, 'main/index.html',
                  {'title': 'Главная страница сайта',
                   'tasks':  tasks})


def about(request):
    return render(request, 'main/about.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма заполнена неверно'
    form = TaskForm()
    context = {
        'form' : form,
        'error': error
    }
    return render(request, 'main/create.html', context)

# Форма для обновления задач - не работает
def update_task(request, title_id):
    task = Task.object.get(pk=title_id)
    form = TaskForm(request.POST or None, instance=title_id)
    if form.is_valid():
        form.save()
        return redirect('home')

    return render(request, 'main/update_task.html', {
        'task' : task,
        'form' : form
    })
