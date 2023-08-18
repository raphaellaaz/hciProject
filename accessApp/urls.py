from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework.documentation import include_docs_urls


router = routers.DefaultRouter()
router.register(r'login', views.loginAppView, 'access')


urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('docs/',include_docs_urls(title='Api Documentation')),
]
