from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages
from .models import *

# Create your views here.
def home_view(request):
    return render(request, 'home.html')

def toLogin_view(request):
    return render(request, 'login.html')

def Login_view(request):
    user = request.POST.get("user", '')
    pwd = request.POST.get("pwd", '')
    if user and pwd:
        c = StudentInfo.objects.filter(stu_name=user,stu_pwd=pwd).count()#获取models里studentinfo类对象的值
        if c >= 1:
            return render(request, 'index.html')
        else:
            messages.success(request, "用户名或密码错误")
            return render(request, 'login.html')
    else:
        messages.success(request, "用户名或密码为空")
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
            messages.success(request, "用户名已存在")
            return render(request, 'register.html')
        elif pwd != confirm_pwd:
            messages.success(request, "密码不一致")
            return render(request, 'register.html')
        else:
            if role == "teacher":
                stu_role = '1'
            else:
                stu_role = '0'
            stu = StudentInfo(stu_id=stu_id,stu_name=user,stu_pwd=pwd,stu_email=email,stu_course=course,stu_role=stu_role)
            stu.save()
            messages.success(request, '注册成功')
            return render(request, 'login.html')
    else:
        messages.success(request, "请补全信息")
        return render(request, 'register.html')