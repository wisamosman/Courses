from django.urls import path
from .views import CoursList, CoursDetail ,add_review

app_name = 'Courses'

urlpatterns = [
    path('',CoursList.as_view(),name='cours_list'),
    path('<slug:slug>',CoursDetail.as_view(),name='cours_detail'),
    path('<slug:slug>/review/add',add_review,name='add_review'),
]