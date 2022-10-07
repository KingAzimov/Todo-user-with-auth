from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .models import *

def todo(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            TODO.objects.create(
                title=request.POST.get('s'),
                description=request.POST.get('d'),
                time=request.POST.get('t'),
                status=request.POST.get('st'),
                student=Student.objects.get(user=request.user)
            )
            return redirect('/todo/')
        data={
            'todo':TODO.objects.filter(student__user=request.user)
        }
        return render(request, 'todo.html', data)
    else:
        return redirect('/')

def loginview(request):
    if request.method=='POST':
        user = authenticate(username=request.POST.get('l'),password=request.POST.get('p'))
        if user is None:
            return redirect('/')
        login(request, user)
        return redirect('/todo/')
    return render(request, 'login.html')

def logoutview(request):
    logout(request)
    return redirect('/')

def register(request):
    if request.method == 'POST':
        u = User.objects.create_user(
            username=request.POST.get('l'),
            password=request.POST.get('p')
        )
        Student.objects.create(
            fullname=request.POST.get('fl'),
            guruh=request.POST.get('g'),
            st_raqam=request.POST.get('st'),
            tel=request.POST.get('t'),
            user=u
        )
        return redirect('/')
    return render(request, 'register.html')

def ochirish(request, son):
    t = TODO.objects.get(id=son)
    if request.user == t.student.user:
        t.delete()
    return redirect('/todo/')