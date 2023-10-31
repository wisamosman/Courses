from django.shortcuts import render
from .models import Courses,Review,Brand
from django.views import generic
from .forms import ReviewForm



# Create your views here.

class CoursList(generic.ListView):
    model = Courses
    paginate_by = 8

    def get_queryset(self):
        brand =  Brand.objects.all()
        queryset = Courses.objects.all()
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["brand"] = Brand.objects.all()
        print(context)
        return context



class CoursDetail(generic.DetailView):
    model = Courses


class BrandList(generic.ListView):
    model = Brand

#def add_review(request,slug):
    #cours = Courses.objects.get(id=id)
    #form = ReviewForm(request.POST)
    #if form.is_valid():
        #myform = form.save(commit=False)
        #myform.user = request.user
        #myform.cours = cours
        #myform.save()
        #return redirect(f'/courses/{cours.id}')