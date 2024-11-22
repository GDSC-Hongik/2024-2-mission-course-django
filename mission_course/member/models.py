from django.db import models

# Create your models here.
class User(models.Model):
    id = models.AutoField(primary_key=True)  # 기본 키로 설정
    name = models.CharField(max_length=100, null=False)  # 필수 입력
    email = models.EmailField(unique=True, null=False)  # 중복 불가, 필수 입력
    birth_date = models.DateField(null=True, blank=True)  # 선택 입력
    join_date = models.DateTimeField(auto_now_add=True)  # 자동으로 가입 일자 생성

    def __str__(self):
        return f"{self.name} ({self.email})"