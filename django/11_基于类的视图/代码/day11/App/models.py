from django.db import models

# Create your models here.
class User(models.Model):
    uid = models.AutoField(primary_key=True)
    username = models.CharField(max_length=30)
    password = models.CharField(db_column='password_hash',max_length=90)

    class Meta:
        db_table = 'bbs_user'