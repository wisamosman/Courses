from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MaxValueValidator,MinValueValidator
from taggit.managers import TaggableManager

# Create your models here.


class Courses(models.Model):
    name = models.CharField(max_length=30)
    subtitle = models.TextField(max_length=100)
    description = models.TextField(max_length=1000)
    image = models.ImageField(upload_to='courses')
    price = models.FloatField()
    tags = TaggableManager()

    def __str__(self):
        return self.name
    



class Review(models.Model):
    user = models.ForeignKey(User,related_name='user_review',on_delete=models.SET_NULL,null=True,blank=True)
    cours = models.ForeignKey(Courses,related_name='cours_review',on_delete=models.SET_NULL,null=True,blank=True)
    review = models.TextField(max_length=500)
    rate = models.IntegerField(validators=[MaxValueValidator(5),MinValueValidator(0)]) 
    create_date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return f"{self.user}-{self.cours}"