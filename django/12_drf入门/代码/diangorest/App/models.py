from django.db import models


# Create your models here.
class BookInfo(models.Model):
    id = models.AutoField(primary_key=True)
    btitle = models.CharField(max_length=200)
    bpub_date = models.DateField(auto_now_add=True,null=True)
    bread = models.IntegerField(default=0)
    bcomment = models.IntegerField(default=0)
    bimage = models.CharField(max_length=200,null=True)

    class Meta:
        db_table = 'bookinfo'