from django.contrib import admin
from django.urls import path,include 
from rest_framework.routers import DefaultRouter
from . import views

#router에 대한 정의

router = DefaultRouter()
router.register('post',views.PostViewSet)   

urlpatterns = [
    path('',include(router.urls))
]