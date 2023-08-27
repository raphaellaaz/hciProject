from django.contrib import admin
from django.urls import path, include
from . import views
from rest_framework import routers
from rest_framework.documentation import include_docs_urls


router = routers.DefaultRouter()
router.register(r'user', views.userAppView, 'user')
router.register(r'solutions', views.solutionsAppView, 'solutions')
router.register(r'tsol', views.typeSolAppView, 'tsol')
router.register(r'negocios', views.negociosAppView, 'negocios')
router.register(r'tuser', views.typeUserAppView, 'tuser')
router.register(r'estadosol', views.estadoSolAppView, 'estado')
router.register(r'infosol', views.infoSolAppView, 'info')
router.register(r'suscritos', views.suscritosAppView, 'suscritos')
router.register(r'trabaja', views.trabajaAppView, 'trabaja')



urlpatterns = [
    path('api/v1/', include(router.urls)),
    path('docs/',include_docs_urls(title='Api Documentation')),
]
