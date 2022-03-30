from django.urls import path, include
from rest_framework.routers import DefaultRouter
from api import views

router = DefaultRouter()

# Record Api
router.register('record', views.RecordAPI, basename='RecordAPI')

urlpatterns = [
    path('', include(router.urls))
]