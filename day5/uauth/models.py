from django.db import models


# Create your models here.
class Users(models.Model):
    u_name = models.CharField(max_length=10)
    u_password = models.CharField(max_length=225)
    # 存在服务器中的cookie的值
    u_ticket = models.CharField(max_length=30, null=True)

    class Meta:
        db_table = 'day51_uesr'


