import os
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.conf import settings

# Create your models here.
class MyUserManager(BaseUserManager):
    def create_user(self, username, full_name, phonenumber,
                    github_address, image=None, password=None, is_hanyoung=False, is_wps=False):

        # 만약 사용자가 사진을 입력 안 했다면, 기본 이미지를 사용함.
        if not image:
            image = os.path.join(settings.STATIC_DIR, 'images/default_user_image.jpg')
        user = self.model(
            username=username,
            full_name=full_name,
            phonenumber=phonenumber,
            image=image,
            github_address=github_address,
        )
        user.set_password(password)
        user.save()
        return user


    def create_hanyoung_user(self, username, full_name, phonenumber,
                             github_address, image=None, password=None, is_hanyoung=True,
                             is_wps=False):
        # 만약 사용자가 사진을 입력 안 했다면, 기본 이미지를 사용함.
        if not image:
            image = os.path.join(settings.STATIC_DIR, 'images/default_user_image.jpg')

        user = self.model(
            username=username,
            full_name=full_name,
            phonenumber=phonenumber,
            image=image,
            github_address=github_address,
        )
        user.set_password(password)
        user.is_hanyoung = True
        user.save()
        return user


    def create_wps_user(self, username, full_name, phonenumber,
                             github_address, image=None, password=None, is_hanyoung=False,
                        is_wps=True):
        # 만약 사용자가 사진을 입력 안 했다면, 기본 이미지를 사용함.
        if not image:
            image = os.path.join(settings.STATIC_DIR, 'images/default_user_image.jpg')

        user = self.model(
            username=username,
            full_name=full_name,
            phonenumber=phonenumber,
            image=image,
            github_address=github_address,
        )
        user.set_password(password)
        user.is_wps = True
        user.save()
        return user


class MyUser(AbstractBaseUser, PermissionsMixin):
    # 모든 회원 필수 사항
    username = models.CharField(max_length=15, unique=True)
    full_name = models.CharField(max_length=20)
    phonenumber = models.CharField(max_length=14)
    image = models.ImageField(upload_to='photo', blank=True, null=True)
    github_address = models.URLField(max_length=50, blank=True)


    # 특수관계인 사항
    is_hanyoung = models.BooleanField(default=False)
    is_wps = models.BooleanField(default=False)

    # 주요 유저네임 필드
    USERNAME_FIELD = 'username'

    # 모델 매니저 설정
    objects = MyUserManager()
