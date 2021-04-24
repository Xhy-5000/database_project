from django.shortcuts import render
from django.db import connection
from django.contrib import messages
from .models import *

# Create your views here.
def home_view(request):
    return render(request, 'home.html')

def toLogin_view(request):
    link = '../index/'
    return render(request, 'login.html', {'link':link})

def Login_view(request):
    user = request.POST.get("user", '')
    pwd = request.POST.get("pwd", '')
    link = "../torewriteinfo/"
    if user and pwd:
        c0 = StudentInfo.objects.filter(stu_name=user,stu_pwd=pwd, stu_role='0').count()#获取models里studentinfo类对象的值
        c1 = StudentInfo.objects.filter(stu_name=user, stu_pwd=pwd, stu_role='1').count()
        if c0 >= 1:
            for student in StudentInfo.objects.all():
                if student.stu_name == user:
                    break
            link = link + user + '/'
            add_and_drop_link = './' + user + '/add_and_drop/'
            return render(request, 'studentindex0.html', context={'student': student, 'link':link, 'add_and_drop_link':add_and_drop_link})
        elif c1 >= 1:
            for student in StudentInfo.objects.all():
                if student.stu_name == user:
                    break
            link = link + user
            return render(request, 'teacherindex0.html', context={'teacher': student, 'link':link})
        else:
            messages.success(request, "Something wrong with your username or password")
            return render(request, 'login.html')
    else:
        messages.success(request, "Username or password missing")
        return render(request, 'login.html')

def toregister_view(request):
    return render(request, 'register.html')

def register_view(request):
    role = request.POST.get("role", '')
    user = request.POST.get("user", '')
    pwd = request.POST.get("pwd", '')
    confirm_pwd = request.POST.get("confirm_pwd", '')
    email = request.POST.get("email", '')
    stu_id = request.POST.get("id", '')
    course = request.POST.get("course", '')
    if role and user and pwd and confirm_pwd and email and id and course:
        c = StudentInfo.objects.filter(stu_name=user).count()
        if c:
            messages.success(request, "User name already exists")
            return render(request, 'register.html')
        elif pwd != confirm_pwd:
            messages.success(request, "Please confirm your password")
            return render(request, 'register.html')
        else:
            if role == "teacher":
                stu_role = '1'
            else:
                stu_role = '0'
            stu = StudentInfo(stu_id=stu_id,stu_name=user,stu_pwd=pwd,stu_email=email,stu_course=course,stu_role=stu_role)
            stu.save()
            # messages.success(request, 'Success')
            return render(request, 'login.html')
    else:
        # messages.success(request, "Lack of some information")
        return render(request, 'register.html')

def toRewrite_view(request, link):
    link = '../../rewriteinfo/' + link + '/'
    return render(request, 'rewriteinfo.html', context= {'link':link})

def Rewrite_view(request, link):
    for student in StudentInfo.objects.all():
        if student.stu_name == link:
            break
    link = '../../index/' + link + '/'
    email = request.POST.get("email", '')
    stu_id = request.POST.get("id", '')
    if stu_id and email:
        stu_name = student.stu_name
        pwd = student.stu_pwd
        course = student.stu_course
        role = student.stu_role
        StudentInfo.objects.get(stu_name=stu_name).delete()
        stu = StudentInfo(stu_id=stu_id, stu_name=stu_name, stu_pwd=pwd, stu_email=email, stu_role=role,
                          stu_course=course)
        stu.save()
        # messages.success(request, "Success")
        if stu.stu_role == '0':
            return render(request, 'studentindex.html', context={'student': stu, 'link': link})
        elif stu.stu_role == '1':
            return render(request, 'teacherindex.html', context={'teacher': stu, 'link': link})
    else:
        messages.success(request, "Lack of some information")
        return render(request, 'rewriteinfo.html', context= {'link':link})

def index_view(request, link):
    for student in StudentInfo.objects.all():
        if student.stu_name == link:
            break
    link = '../../torewriteinfo/' + link + '/'
    if student.stu_role == 1:
        return render(request, 'teacherindex.html', context={'teacher': student, 'link':link})
    else:
        return render(request, 'studentindex.html', context={'student': student, 'link':link})

def add_and_drop_view(request, user_name):
    for user in StudentInfo.objects.all():
        if user.stu_name == user_name:
            break
    courses_ids = user.stu_course.split(',')
    courses = []
    for course in CourseInfo.objects.all():
        if course.course_id in courses_ids:
            courses.append(course)
    return render(request, 'add_and_drop.html', context={'user':user, 'courses':courses})






