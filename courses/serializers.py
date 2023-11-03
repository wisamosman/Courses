from rest_framework import serializers
from .models import Courses, Brand



class CoursSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courses
        fields = '__all__'