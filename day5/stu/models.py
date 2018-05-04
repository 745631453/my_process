from django.db import models


class Student(models.Model):
    s_name = models.CharField(max_length=10)
    s_tel = models.CharField(max_length=11)

    class Meta:
        db_table = 'day5_stu'


class StudentInfo(models.Model):
    i_addr = models.CharField(max_length=30)
    s = models.OneToOneField(Student)
    i_image = models.ImageField(upload_to='upload',null=True)

    class Meta:
        db_table = 'day5_stuinfo'


class Visit(models.Model):

    v_url = models.CharField(max_length=30)
    v_time = models.IntegerField()

    class Meta:
        db_table = 'visit'
