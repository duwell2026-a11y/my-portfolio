from django.contrib import admin
from django import forms
from .models import Project, ProjectImage

# 1. 여러 파일을 받기 위한 커스텀 위젯 설정
class MultipleFileInput(forms.ClearableFileInput):
    allow_multiple_selected = True

class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result

# 2. 관리자 페이지용 폼 생성
class ProjectAdminForm(forms.ModelForm):
    images_field = MultipleFileField(label='상세 이미지 일괄 등록 (여러 장 선택 가능)', required=False)

    class Meta:
        model = Project
        fields = '__all__'

# 3. Project 관리자 설정
class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    form = ProjectAdminForm
    inlines = [ProjectImageInline]

    def save_model(self, request, obj, form, change):
        # 먼저 프로젝트 자체를 저장
        super().save_model(request, obj, form, change)
        
        # 일괄 등록 필드에서 파일들을 가져와서 하나씩 저장
        files = request.FILES.getlist('images_field')
        for f in files:
            ProjectImage.objects.create(project=obj, image=f)