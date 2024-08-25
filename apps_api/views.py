from django.shortcuts import render
from rest_framework import viewsets
from apps_api.models import Course
from apps_api.models import Instances
from apps_api.serializers import CourseSerializer
from apps_api.serializers import InstancesSerializer

# Create your views here.
class CourseViewSet(viewsets.ModelViewSet):
    queryset=Course.objects.all()
    serializer_class=CourseSerializer

class InstancesViewSet(viewsets.ModelViewSet):
    queryset=Instances.objects.all()
    serializer_class=InstancesSerializer


