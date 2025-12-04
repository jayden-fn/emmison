from django.shortcuts import render,redirect
from .forms import  CreateUserForm, LoginForm
from django.contrib.auth.models import auth 
from django.contrib.auth import authenticate

# Create your views here.
def home(request):
    return render(request, 'website/index.html')

#register a user 
def register(request):
    form = CreateUserForm()

    if request.method =="POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
        
        context = {'form': form}

        return render(request,'website/register.html', context=context)
    
#login a user 
def my_login(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)

            if user is not None:
                auth.login(request, user)
                #return redirect('home')
    
    context = {'form': form}
    return render(request, 'website/my-login.html', context=context)