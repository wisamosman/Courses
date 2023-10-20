from django.contrib import admin
from .models import Courses , Review
# Register your models here.

class CoursAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name','subtitle']

admin.site.register(Courses,CoursAdmin)
admin.site.register(Review)