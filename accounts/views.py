from django.shortcuts import render, redirect
from django.views.decorators.http import require_http_methods



from django.contrib.auth import (
    authenticate,
    get_user_model,
    login,
    logout
)
from .forms import userLogin, userRegister

@require_http_methods(["GET", "POST"])
def loginview(request):
    next = request.GET.get('next')
    form = userLogin(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        if next:
            return redirect(next)
        return redirect('/')
    context = {'form':form}
    return render(request, 'reglog.html', context)

@require_http_methods(["GET", "POST"])           
def signin(request):
    next = request.GET.get('next')
    form = userRegister(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect('/accounts/login/')
    context = {'form':form}
    return render(request, 'signin.html', context)

            
def logoutview(request):
    logout(request)
    return redirect('/accounts/login')