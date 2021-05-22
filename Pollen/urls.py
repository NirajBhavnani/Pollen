from django.urls import path
from . import views
app_name = 'Pollen'

urlpatterns = [
    path('', views.home, name="home"),
    path('pollen_info/', views.pollen_info, name="pollen_info"),
    path('pollen_help/', views.pollen_help, name="pollen_help"),
    path('health/', views.health, name="health"),
    path('predict/', views.predict, name="predict"),
    path('predict/city/', views.predictCity, name="predictCity"),
    path('classify/', views.classify, name="classify"),
    path('classify/taxa/', views.classifyTaxa, name="classifyTaxa"),
]