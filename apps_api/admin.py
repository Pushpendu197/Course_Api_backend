from django.contrib import admin
from apps_api.models import Course
from apps_api.models import Instances

# Register your models here.
admin.site.register(Course)
admin.site.register(Instances)