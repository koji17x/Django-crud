from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.db import IntegrityError
from .forms import taskform, AdvanceForm
from .models import Task, Advance
from django.utils import timezone
from django.contrib.auth.decorators import login_required


def home(request):
    return render(request, "home.html")


def signup(request):

    if request.method == "GET":
        return render(request, "signup.html", {
            "form": UserCreationForm
        })
    else:
        if request.POST["password1"] == request.POST["password2"]:
            try:
                user = User.objects.create_user(
                    username=request.POST["username"], password=request.POST["password1"])
                user.save()
                login(request, user)
                return redirect("tasks")
            except IntegrityError:
                return render(request, "signup.html", {
                    "form": UserCreationForm,
                    "error": "El usuario ya existe"
                })

        return render(request, "signup.html", {
            "form": UserCreationForm,
            "error": "La contraseña no coincide"
        })

@login_required
def tasks(request):
    tasks = Task.objects.filter(user=request.user, datacompleted__isnull=True)
    return render(request, "tasks.html", {"tasks": tasks, "tasks_type":"Tareas Pendientes"})

@login_required
def signout(request):
    logout(request)
    return redirect("home")


def signin(request):
    if request.method == "GET":
        return render(request, "signin.html", {
            "form": AuthenticationForm
        })
    else:
        user = authenticate(
            request, username=request.POST["username"], password=request.POST["password"])
        if user is None:
            return render(request, "signin.html", {
                "form": AuthenticationForm,
                "error": "Usuario o contraseña incorrectos"
            })
        else:
            login(request, user)
            return redirect("tasks")

@login_required
def create_task(request):
    if request.method == "GET":
        return render(request, "create_task.html", {
            "form": taskform
        })
    else:
        try:
            form = taskform(request.POST)
            new_task = form.save(commit=False)
            new_task.user = request.user
            new_task.save()
            return redirect("tasks")
        except ValueError:
            return render(request, "create_task.html", {
                "form": taskform,
                "error": "Por favor provee datos validos"
            })

@login_required
def task_detail(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    advances = Advance.objects.filter(task=task)
    error = None
    
    if request.method == "GET":
        form = taskform(instance=task)
        advance_form = AdvanceForm()
        return render(request, "task_detail.html", {"task": task, "form": form, "advance_form": advance_form, "advances": advances, "error": error})
    
    elif request.method == "POST":
        if 'save_task' in request.POST:
            form = taskform(request.POST, instance=task)
            if form.is_valid():
                form.save()
                return redirect("tasks")

        elif 'add_advance' in request.POST:
            if task.datacompleted:
                error = "No puedes agregar avances a una tarea completada."
            else:
                advance_form = AdvanceForm(request.POST)
                if advance_form.is_valid():
                    new_advance = advance_form.save(commit=False)
                    new_advance.task = task
                    new_advance.save()
                    return redirect("task_detail", task_id=task.id)
                
    form = taskform(instance=task)
    advance_form = AdvanceForm()
    return render(request, "task_detail.html", {"task": task, "form": form, "advance_form": advance_form, "advances": advances, "error": "Error al procesar la solicitud"})

@login_required
def complete_task(request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == "POST":
        task.datacompleted = timezone.now()
        task.save()
        return redirect("tasks")

@login_required
def delete_task (request, task_id):
    task = get_object_or_404(Task, pk=task_id, user=request.user)
    if request.method == "POST":
        task.delete()
        return redirect("tasks")
    

@login_required
def tasks_completed(request):
    tasks = Task.objects.filter(user=request.user, datacompleted__isnull=False).order_by("-datacompleted")
    return render(request, "tasks.html", {"tasks": tasks, "tasks_type":"Tareas Completadas"})