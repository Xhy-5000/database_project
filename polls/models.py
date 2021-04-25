from django.db import models

# Create your models here.
class StudentInfo(models.Model):
    stu_id = models.CharField(primary_key=True, max_length=20)
    stu_name = models.CharField(max_length=20)
    stu_pwd = models.CharField(max_length=20)
    stu_email = models.CharField(max_length=50)
    stu_course = models.CharField(max_length=100)
    stu_role = models.CharField(max_length=1)



class CourseInfo(models.Model):
    course_id = models.CharField(primary_key=True, max_length=20)
    course_name = models.CharField(max_length=50)
    course_instructor = models.CharField(max_length=20)
    course_description = models.CharField(max_length=1000)

class Studentmark(models.Model):
    mark_id = models.CharField(primary_key=True, max_length=20)
    stu_id = models.CharField(max_length=20)
    stu_name = models.CharField(max_length=20)
    course_id = models.CharField(max_length=20)
    assignment_1 = models.CharField(max_length=20)
    assignment_2 = models.CharField(max_length=20)
    assignment_3 = models.CharField(max_length=20)
    assignment_4 = models.CharField(max_length=20)
    assignment_5 = models.CharField(max_length=20)
    assignment_6 = models.CharField(max_length=20)
