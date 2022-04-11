from django.db import models
import os

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    head_image = models.ImageField(upload_to='classnote/images/%Y/%m/%d/', blank=True)
    file_upload = models.FileField(upload_to='classnote/files/%Y/%m/%d/', blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)    #업데이트필드(시간자동입력) 생성

    # 포스트 생성시, '[id] title' 표현하도록 함
    def __str__(self):
        return f'[{self.pk}] {self.title}'
    # post 주소
    def get_absolute_url(self):
        return f'/classnote/{self.pk}/'

    # 업로드파일 이름 가져오는 함수
    def get_file_name(self):
        return os.path.basename(self.file_upload.name)

    # 업로드파일 확장자 가져오는 함수
    def get_file_ext(self):
        return self.get_file_name().split('.')[-1]