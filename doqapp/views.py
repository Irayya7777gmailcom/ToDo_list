from django.shortcuts import render,redirect
from .models import task
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from . forms import signupform

def login(request):
    return render(request,'login.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request)
            return redirect('/get_task')  
        else:
            error_message = "Invalid username or password."
            return render(request, 'login.html', {'error_message': error_message})
    return render(request, 'login.html')

def signup(request):
    if request.method == 'POST':
        form = signupform(request.POST)
        if form.is_valid():
            form.save()
            
            return redirect('/login_view')  
    else:
        form = signupform()
    return render(request, 'signup.html', {'form': form})

def task_list(request):
    return render(request,'form.html')


def create_task(request):
    
      if request.method=='POST':

        x=request.POST['title']
        y=request.POST['desc']
        z=request.POST['due_date']
        w=request.POST['status']
    
        c1=task.objects.create(Title=x,description=y,due_date=z,completion_status=w)
        c1.save()
      return redirect('/get_task')

def get_task(request):
    content={}
    content['data']=task.objects.all()
    
    return render(request,'dashboard.html',content)


def edit(request,rid):
     if request.method=='POST':
        x=request.POST['title']
        y=request.POST['desc']
        z=request.POST['due_date']
        w=request.POST['status']
        c=task.objects.filter(id=rid)
        c.update(Title=x,description=y,due_date=z,completion_status=w)
        return redirect('/get_task')
     else:
     
         content={}
         content['data']=task.objects.get(id=rid)
         return render(request,'edit_task.html',content)
    

def delete(request,rid):
    x=task.objects.get(id=rid)
    x.delete()
    return redirect('/get_task')


