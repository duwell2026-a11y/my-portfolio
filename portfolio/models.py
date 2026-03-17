# portfolio/models.py
from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=200, verbose_name="프로젝트 제목")
    # 내용(설명) 필드 추가
    content = models.TextField(blank=True, verbose_name="프로젝트 설명") 
    thumbnail = models.ImageField(upload_to='thumbnails/', verbose_name="썸네일 이미지")
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

# 상세페이지용 이미지를 여러 장 담을 모델 추가
class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name='images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='details/')
    order = models.IntegerField(default=0, verbose_name="순서") # 이미지 순서 정하기

    class Meta:
        ordering = ['order'] # 설정한 순서대로 정렬