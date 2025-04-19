from django.shortcuts import render,redirect
from .forms import LoginForm
from django.contrib.auth.models import User
from django.contrib.auth import login,authenticate
def loginView(request):
    form = LoginForm(request.POST or None)
    context = {'form':form}
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username,password=password)
        if user is not None:
            login(request, user)
            return redirect('/contact')
    return render(request,'compte/login.html',context)
