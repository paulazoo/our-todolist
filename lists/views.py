from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render

from lists.forms import TodoForm
from lists.models import Todo, TodoList


def index(request):
    return render(request, "lists/index.html", {"form": TodoForm()})

@login_required
def todolist(request, todolist_id):
    todolist = get_object_or_404(TodoList, pk=todolist_id)
    if request.method == "POST":
        redirect("lists:add_todo", todolist_id=todolist_id)

    return render(
        request, "lists/todolist.html", {"todolist": todolist, "form": TodoForm()}
    )

def add_todo(request, todolist_id):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            user = request.user if request.user.is_authenticated else None
            todo = Todo(
                description=request.POST["description"],
                info=request.POST["info"],
                todolist_id=todolist_id,
                creator=user,
            )
            todo.save()
            return redirect("lists:todolist", todolist_id=todolist_id)
        else:
            return render(request, "lists/todolist.html", {"form": form})

    return redirect("lists:index")