from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

# 自己的用户模型必须继承AbstractUser
class User(AbstractUser):
    phone = models.CharField(max_length=50,null=True)

    class Meta:
        db_table = 'user'

