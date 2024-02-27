from django.http import JsonResponse
from rest_framework import generics
from ..models import project
from ..serializers import projectserializer

def index(request):
    return JsonResponse({'message': 'Hello from Django!'})

def get_data(request):
    data = {'message': 'Dados do backend'}
    return JsonResponse(data)

# class ProjectList(generics.ListCreateAPIView):
#     queryset = project.objects.all()
#     serializer_class = projectserializer