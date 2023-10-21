from django.urls import path
from .views import CoursList, CoursDetail 

app_name = 'Courses'

urlpatterns = [
    path('',CoursList.as_view(),name='cours_list'),
    path('<int:pk>',CoursDetail.as_view(),name='cours_detail'),
    #path('<int:id>/review/add',add_review,name='add_review'),
]