from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from .models import *

# Create your views here.
def home_view(request):
    return render(request, 'home.html')

def toLogin_view(request):
    return render(request, 'login.html')

def Stu_view(request):
    student = request.user
    return render(request, 'studentindex.html',context={'student': student})

def Login_view(request):
    user = request.POST.get("user", '')
    pwd = request.POST.get("pwd", '')
    if user and pwd:
        c0 = StudentInfo.objects.filter(stu_name=user,stu_pwd=pwd, stu_role='0').count()#获取models里studentinfo类对象的值
        c1 = StudentInfo.objects.filter(stu_name=user, stu_pwd=pwd, stu_role='1').count()
        if c0 >= 1:
            for student in StudentInfo.objects.all():
                if student.stu_name == user:
                    break
            return render(request, 'studentindex.html', {'student': student})
        elif c1 >= 1:
            for student in StudentInfo.objects.all():
                if student.stu_name == user:
                    break
            return render(request, 'teacherindex.html', {'teacher': student})
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
    if role and user and pwd and confirm_pwd and email and id:
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
            messages.success(request, 'Success')
            return render(request, 'login.html')
    else:
        messages.success(request, "Lack of some information")
        return render(request, 'register.html')