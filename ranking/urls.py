from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.div1, name='mainpage'),
    path('div1/', views.div1, name='div1ranking'),
    path('div2/', views.div2, name='div2ranking'),
    path('div3/', views.div3, name='div3ranking'),
]