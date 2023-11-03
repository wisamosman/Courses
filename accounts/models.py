from django.db import models
from django.contrib.auth.models import User
from utils.generate_code import generate_code

# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User,related_name='user_profile',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='accounts')
    code = models.CharField(max_length=10,default=generate_code)

    def __str__(self):
        return str(self.user)
    


class Phones(models.Model):
    user = models.ForeignKey(User,related_name='user_phones',on_delete=models.CASCADE)
    type = models.CharField(max_length=10)
    phone = models.CharField(max_length=10)


    def __str__(self):
        return str(self.user)




