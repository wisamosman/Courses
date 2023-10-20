from django.shortcuts import render
from .models import Courses,Review
from django.views import generic



# Create your views here.

class CoursList(generic.ListView):
    model = Courses