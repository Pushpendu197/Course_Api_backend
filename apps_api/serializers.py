from rest_framework import serializers
from apps_api.models import Course
from apps_api.models import Instances

class CourseSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Course
        fields = ['course_id','course_title','course_code','course_desc']



class InstancesSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Instances
        fields = ['instances_id','instances_title','instances_year','instances_sem']
        