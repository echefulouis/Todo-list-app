from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.utils import timezone
from .models import Todo,Done
from django.urls import reverse

# Create your views here.

def index(request):
    todo_items= Todo.objects.all().order_by('-added_date')
    length_of_created_obj= Todo.objects.all().count()
    
    done_items= Done.objects.all().order_by('-done_date')
    length_of_done_items= Done.objects.all().count()
    return render(request, 'main/index.html', {'todo_items':todo_items, 
                                               'length_of_items': length_of_created_obj, 
                                               'done_items':done_items ,
                                               'length_of_done_items':length_of_done_items})

def add_todo(request):
    #Collected the Input passed as a request and stored it to a variable 'task'
    task=request.POST.get('task')

    #created a time record of the input
    date_added=timezone.now()

    #created an object to store this inputs in the data base
    Todo.objects.create(text=task, added_date=date_added)
    return HttpResponseRedirect('/')

def delete_todo(request, todo_id):
    # collected the text data to be done
    task_done_text = Todo.objects.get(id=todo_id).text
    
    # collected the text data date
    task_done_text_date = Todo.objects.get(id=todo_id).added_date
    
    #deleted the task that's done
    Todo.objects.get(id=todo_id).delete()
    
    # added the tasks thats done in the done table
    Done.objects.create(done_text=task_done_text, done_date=task_done_text_date)
    return HttpResponseRedirect('/')

def Done_todo(request, done_id):
    Done.objects.get(id=done_id).delete()
    return HttpResponseRedirect('/')






