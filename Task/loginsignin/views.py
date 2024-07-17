from django.shortcuts import render , redirect ,get_object_or_404
from .forms import CreateUserForm, LoginForm, CreateTask
# - Authentication models and functions

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Task
from .models import User
from django.contrib.auth import get_user_model
# Create your views here.

def homepage(request):
    return(render(request, 'loginsignin/index.html'))

def register(request):
    
    form = CreateUserForm()
    
    if request.method == "POST":
        
        form = CreateUserForm(request.POST)
        
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            admin = request.POST.get('is_staff')
            print(admin)
            username = request.POST.get('username')
            password = request.POST.get('password')
            if admin is not None:
                return redirect("adminpass1")
            else:
                messages.success(request, 'Account was created for ' + user )
            
                return redirect("login")
        
    
    context = {'registerform':form} 
    
    return(render(request, 'loginsignin/register.html',context=context))

def login(request):
    
    form = LoginForm()
    if request.method == 'POST':
        form = LoginForm(request,data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            
            user = authenticate(request, username=username , password=password)
            if user is not None :
                auth.login(request, user)
                if user.is_staff:
                    return redirect("adminpass")
                else:
                    return redirect("dashboard")
            else:
               messages.success(request,'Username OR Password is incorrect.')
    
    context = {'loginform': form}
    
    return(render(request, 'loginsignin/login.html',context=context))



def user_logout(request):
    
     auth.logout(request)
     
     return redirect("")


@login_required(login_url="login")
def adminpass(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        if password =="password":
            return redirect("admin_dash")
        else:
            return redirect("")
    return(render(request, 'loginsignin/adminpass.html'))




def adminpass1(request):
    if request.method == 'POST':
        password = request.POST.get('password')
        if password =="password":
            return redirect("login")
        else:
            return redirect("adminpass1")
    return(render(request, 'loginsignin/adminpass1.html'))



@login_required(login_url="login")
def dashboard(request):
    return(render(request, 'profile/dashboard.html'))




@login_required(login_url="login")
def admin_dash(request):
    return(render(request, 'profile/admin_dash.html'))




@login_required(login_url="login")
def create_task(request):
    form = CreateTask()
    if request.method == 'POST':
        form=CreateTask(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect('dashboard')
    context={'create_taskform':form}
    return(render(request, 'profile/create_task.html',context=context))
    

@login_required(login_url="login")
def view_task(request):
   current_user = request.user.id
   task = Task.objects.all().filter(user=current_user)
   context={'task':task}
   return(render(request, 'profile/view_task.html',context=context))

@login_required(login_url="login")
def update_task(request, pk):
    task = Task.objects.get(id=pk)
    form = CreateTask(instance=task)
    if request.method == 'POST':
        form = CreateTask(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect('view_task')
    context = {'updatetask':form}
    return(render(request, 'profile/update_task.html',context=context))


@login_required(login_url="login")
def delete_task(request,pk):
    task = Task.objects.get(id=pk)
    if request.method == 'POST':
        task.delete()
        return redirect ('view_task')
    return(render(request, 'profile/delete_task.html'))
    
    
@login_required(login_url="login")
def create_user(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect('admin_dash')
    context={'create_userform':form}
    return(render(request, 'profile/create_user.html',context=context))
    

@login_required(login_url="login")
def view_user(request):
    User = get_user_model()
    users = User.objects.all()
    context={'users':users}
    return(render(request, 'profile/view_user.html',context=context))

@login_required(login_url="login")
def update_user(request, pk):
    User = get_user_model()
    users = User.objects.get(id=pk)
    print(users)
    form = CreateUserForm(instance=users)
    if request.method == 'POST':
        form = CreateUserForm(request.POST, instance=users)
        if form.is_valid():
            form.save()
            return redirect('view_user')
    context = {'updateuser':form}
    return(render(request, 'profile/update_user.html',context=context))


@login_required(login_url="login")
def delete_user(request, pk):
    user = User.objects.get(id=pk)
    id=pk
    if user == user or user.is_superuser:
        if request.method == 'POST':
            user.delete()
            return redirect ('view_user')
    return(render(request, 'profile/delete_user.html'))

    