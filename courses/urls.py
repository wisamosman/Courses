from django.urls import path
from .views import CoursList, CoursDetail , BrandList
from .api import cours_list_api

app_name = 'Courses'

urlpatterns = [
    path('',CoursList.as_view(),name='cours_list'),
    path('<slug:slug>',CoursDetail.as_view(),name='cours_detail'),
    path('brand/',BrandList.as_view(),name='brand_list'),
    #path('<int:id>/review/add',add_review,name='add_review'),
    path('api/list',cours_list_api),
    
]