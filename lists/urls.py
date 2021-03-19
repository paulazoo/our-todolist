from django.urls import path

from lists import views

app_name = "lists"
urlpatterns = [
    path("", views.index, name="index"),
    path("todolist/<int:todolist_id>/", views.todolist, name="todolist"),
    path("todo/add/<int:todolist_id>/", views.add_todo, name="add_todo"),
]
