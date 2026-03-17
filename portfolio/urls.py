# portfolio/urls.py (포트폴리오 폴더 안에 있는 파일입니다!)
from django.urls import path
from . import views

urlpatterns = [
    path('', views.project_list, name='project_list'),
    path('project/<int:pk>/', views.project_detail, name='project_detail'),
]