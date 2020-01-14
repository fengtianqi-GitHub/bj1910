from django.db import models

# Create your models here.
class User(models.Model):
    uid = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=60)
    password_hash = models.CharField(max_length=128)
    sex = models.IntegerField(default=1)

    class Meta:
        db_table = 'bbs_user'