from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse
# Create your views here.
from .models import *
from .apps import FirestoreDB
import json

def index(request):

    if request.method == "POST":
        # extract data from the post request
        data = request.POST
        title = data["title"]

        # create Task object and save it in Firestore
        task = Task(title)
        FirestoreDB.todo_collection.document(title).set(task)
        return redirect('/')

    return render(request, 'tasks/list.html', {})


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
