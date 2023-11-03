from django.contrib import admin
from .models import Profile,Phones

# Register your models here.


class PhonesAdmin(admin.TabularInline):
    model = Phones




class ProfileAdmin(admin.ModelAdmin):
    pass


admin.site.register(Profile,ProfileAdmin)
admin.site.register(Phones)
