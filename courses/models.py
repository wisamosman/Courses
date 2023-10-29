from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.core.validators import MaxValueValidator,MinValueValidator
from taggit.managers import TaggableManager
from django.utils.text import slugify
from django.db.models.aggregates import Avg , Sum,Count

# Create your models here.


class Courses(models.Model):
    name = models.CharField(max_length=30)
    subtitle = models.TextField(max_length=10)
    description = models.TextField(max_length=20)
    image = models.ImageField(upload_to='courses')
    price = models.FloatField()
    tags = TaggableManager()
    video = models.URLField(null=True,blank=True)
    slug = models.SlugField(null=True,blank=True)
    user = models.ForeignKey(User,related_name='user_cours',on_delete=models.SET_NULL,null=True,blank=True)

    def __str__(self):
        return self.name
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)    
        super(Courses, self).save(*args, **kwargs) 


class Review(models.Model):
    user = models.ForeignKey(User,related_name='user_review',on_delete=models.SET_NULL,null=True,blank=True)
    cours = models.ForeignKey(Courses,related_name='cours_review',on_delete=models.SET_NULL,null=True,blank=True)
    review = models.TextField(max_length=500)
    rate = models.IntegerField(validators=[MaxValueValidator(5),MinValueValidator(0)]) 
    create_date = models.DateTimeField(default=timezone.now)


    def __str__(self):
        return f"{self.user}-{self.cours}"
    


class Brand(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='brand')
    slug = models.SlugField(null=True,blank=True)
    user = models.ForeignKey(User,related_name='user_brand',on_delete=models.SET_NULL,null=True,blank=True)
    cours = models.ForeignKey(Courses,related_name='cours_brand',on_delete=models.SET_NULL,null=True,blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)    
        super(Brand, self).save(*args, **kwargs)