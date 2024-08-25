from django.urls import path,include
from rest_framework import routers
from apps_api.views import CourseViewSet
from apps_api.views import InstancesViewSet

router=routers.DefaultRouter()
# /................
router.register(r'course',CourseViewSet) 
router.register(r'instances',InstancesViewSet) 

urlpatterns = [
    path('', include(router.urls)),
]
