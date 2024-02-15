'''
Admin
Admin1234
'''
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from home.models import ToDo

from django.shortcuts import render, redirect
def index(request):
    if not request.user.is_authenticated:
        return redirect("login")
    if request.method == "POST":
        task = request.POST.get("task")
        new_task =ToDo(user=request.user, task=task)
        new_task.save()
    all_task = ToDo.objects.filter(user=request.user)
    context = {
        'tasks': all_task
    }
    return render(request, 'index.html', context)
def register(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if len(password) < 8:
            messages.error(request, "Password must be of 8 characters long")
            return redirect('register')
        get_all_users = User.objects.filter(username = username)
        if get_all_users:
            messages.error(request,"Username already Exists!!!")
            return redirect('register')
        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "User Successfully Registered! You can Login Now")
        return redirect('login')
    return render(request, 'register.html')
def loginUser(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request,user)
            return redirect("/")
        else:
            messages.error(request, "Incorrect Username or Password")
            return redirect("login")
    return render(request, 'login.html')
def logoutUser(request):
    logout(request)
    messages.success(request, "Logged out Successfully")
    return redirect('login')
def deleteTask(request,task):
    get_task = ToDo.objects.get(user=request.user, task=task)
    get_task.delete()
    return redirect('/')
def updateTask(request, task):
    get_task = ToDo.objects.get(user=request.user, task=task)
    get_task.status = True
    get_task.save()
    return redirect('/')
def reset(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        if len(password) < 8:
            messages.error(request, "Password must be of 8 characters long")
            return redirect('reset')
        elif not User.objects.filter(username=username, email=email).exists():
             messages.error(request, "User does not Exists")
             return redirect('reset')
        u = User.objects.get(username=username, email=email)
        u.set_password(password)
        u.save()
        messages.success(request, "Password RESET Successful")
        return redirect('login')
    return render(request,'reset.html')

