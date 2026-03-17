# portfolio/views.py
from django.shortcuts import render, get_object_or_404
from .models import Project

# 1. 메인 목록 화면 (이 이름이 project_list여야 합니다)
def project_list(request):
    projects = Project.objects.all()
    return render(request, 'portfolio/index.html', {'projects': projects})

# 2. 상세 페이지 화면 (이 이름은 project_detail)
def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    return render(request, 'portfolio/detail.html', {'project': project})