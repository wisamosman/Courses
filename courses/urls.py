from django.urls import path
from .views import CoursList

app_name = 'Courses'

urlpatterns = [
    path('',CoursList.as_view(),name='cours_list'),
]