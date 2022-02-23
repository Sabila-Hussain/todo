from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
# Create your views here.
from .models import *
from .forms import *
from .apps import FirestoreDB
import json

def index(request):
    tasks = FirestoreDB.todo_collection.get()
    taskdict = [task.to_dict() for task in tasks]
    form = TaskForm()
    context = {'tasks': taskdict,  'form': form}


    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            FirestoreDB.todo_collection.document(data["title"]).set(data)
            # form.save()
            return redirect('/')
    return render(request, 'tasks/list.html', context)


def updateTask(request, pk):
    # task = Task.objects.get(id=pk)
    doc = FirestoreDB.todo_collection.document(pk)
    task = doc.get()
    form = TaskForm(instance=task)


    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            FirestoreDB.todo_collection.document(pk).set(form.cleaned_data)
            # form.save()
            return redirect('/')

    context = {"form": form}
    return render(request, "tasks/update_task.html", context)

#
# def deleteTask(request, pk):
#     item = Task.objects.get(id=pk)
#     context = {"item": item}
#     if request.method == "POST":
#         item.delete()
#         return redirect('/')
#
#     return render(request, 'tasks/delete.html', context)
