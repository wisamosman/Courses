from django.shortcuts import render,redirect
from .models import Courses,Review
from django.views import generic
from .forms import ReviewForm



# Create your views here.

class CoursList(generic.ListView):
    model = Courses



class CoursDetail(generic.DetailView):
    model = Courses


def add_review(request,slug):
    cours = Courses.objects.get(id=id)
    form = ReviewForm(request.POST)
    if form.is_valid():
        myform = form.save(commit=False)
        myform.user = request.user
        myform.cours = cours
        myform.save()
        return redirect(f'/courses/{cours.id}')