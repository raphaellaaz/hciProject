from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework.documentation import include_docs_urls


router = routers.DefaultRouter()
router.register(r'access', views.accessAppView, 'access')


urlpatterns = [
    path('', views.login, name='loginPage'),
    path('r/', views.register, name='registerPage'),
    path('rc/', views.recover, name='recoverPage'),
    path('api/v1/', include(router.urls)),
    path('docs/',include_docs_urls(title='Api Documentation')),
]
