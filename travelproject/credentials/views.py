from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404

from django.shortcuts import redirect, render


# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,'nextpage.html')
        else:
            messages.info(request,'Invalid Credentials')
            return redirect('login')

    return render(request,'login.html')





def register(request):
    if request.method=='POST':
        username=request.POST['username']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email taken')
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
                user.save();
                print('User created')
                return redirect('login')
        else:
            messages.info(request,'Password not matched')
            return  redirect('register')
        return redirect('/')

    return  render(request,'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def form(request):
    return render(request,'form.html')

def done(request):
    return render(request,'done.html')

def gotoform(request):
    return render(request,'nextpage.html')




