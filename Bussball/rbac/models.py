from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.

# 用户表
class User(AbstractUser):
    avatar = models.ImageField(upload_to='avatar/%Y/%m', default='avatar/default.png', max_length=200,
                               blank=True, null=True, verbose_name="用户头像")
    mobile = models.CharField(max_length=11, blank=True, null=True, verbose_name="手机号")
    url = models.URLField(max_length=100, blank=True, null=True, verbose_name="个人网页地址")
    roles = models.ManyToManyField(to="Role", verbose_name="角色")

    class Meta:
        verbose_name = "用户"
        verbose_name_plural = verbose_name
        ordering = ["-id"]

    def __str__(self):
        return self.username


# 角色表
class Role(models.Model):
    title = models.CharField(max_length=32, verbose_name="角色名称")
    permissions = models.ManyToManyField(to="Permission", verbose_name="权限名称")

    def __str__(self):
        return self.title


# 权限表
class Permission(models.Model):
    title = models.CharField(max_length=32, verbose_name="权限")
    url = models.CharField(max_length=32, verbose_name="权限URL")
    action = models.CharField(max_length=32, default="", verbose_name="action")
    group = models.ForeignKey("PermissionGroup", default=1)

    def __str__(self):
        return self.title


# 权限组表
class PermissionGroup(models.Model):
    title = models.CharField(max_length=32, verbose_name="权限组名称")

    def __str__(self):
        return self.title
