from django.shortcuts import render,redirect
from .models import Profile,Phones
from .forms import SignupForm,ActivateUser


def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()

    else:
        form = SignupForm()

    return render(request,'registration/signup.html',{'form':form})            

# Create your views here.
