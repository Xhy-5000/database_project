from django.db import models

# Create your models here.
class StudentInfo(models.Model):
    stu_id = models.CharField(primary_key=True, max_length=20)
    stu_name = models.CharField(max_length=20)
    stu_pwd = models.CharField(max_length=20)
    stu_email = models.CharField(max_length=50)
    stu_course = models.CharField(max_length=100)
    stu_role = models.CharField(max_length=1)
