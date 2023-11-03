from .serializers import CoursSerializer
from .models import Courses 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import generics



@api_view(['GET'])
def cours_list_api(request):
    courses = Courses.objects.all()[:10]
    data = CoursSerializer(courses,many=True,context=({'request':request})).data
    

    return Response({'data':data})


class CoursDetailAPI(generics.RetrieveDestroyAPIView):
     queryset = Courses.objects.all()
     serializer_class = CoursSerializer
