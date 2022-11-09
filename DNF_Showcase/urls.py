from django.urls import path, include
from rest_framework.routers import DefaultRouter

from DNF_Showcase import views

router = DefaultRouter()
router.register('a', views.A_ViewSet)
router.register('b', views.A_ViewSet)
router.register('c', views.A_ViewSet)
urlpatterns = [path('', include(router.urls))]
