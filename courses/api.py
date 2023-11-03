from .serializers import CoursSerializer
from .models import Courses 
from rest_framework.decorators import api_view
from rest_framework.response import Response



@api_view(['GET'])
def cours_list_api(request):
    courses = Courses.objects.all()
    data = CoursSerializer(courses,many=True).data

    return Response({'data':data})