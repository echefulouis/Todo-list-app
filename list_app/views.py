from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.utils import timezone
from .models import Todo
from django.urls import reverse

# Create your views here.

def index(request):
    todo_items= Todo.objects.all().order_by('-added_date')
    length_of_created_obj= Todo.objects.all().count()

    return render(request, 'main/index.html', {'todo_items':todo_items, 'length_of_items': length_of_created_obj })

def add_todo(request):
    #Collected the Input passed as a request and stored it to a variable 'task'
    task=request.POST.get('task')

    #created a time record of the input
    date_added=timezone.now()

    #created an object to store this inputs in the data base
    Todo.objects.create(text=task, added_date=date_added)
    return HttpResponseRedirect('/')

def delete_todo(request, todo_id):
    return HttpResponseRedirect('/')







