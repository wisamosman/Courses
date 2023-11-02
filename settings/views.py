from django.shortcuts import render
from courses.models import Courses , Brand , Review
# Create your views here.


def home(request):
    brands = Brand.objects.all()
    courses = Courses.objects.all()
    return render(request,'settings/home.html',{'brands':brands,
                                                'courses':courses})