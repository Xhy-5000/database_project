from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.
def toLogin_view(request):
    return render(request, 'login.html')

def Login_view(request):
    user = request.POST.get("user", '')
    pwd = request.POST.get("pwd", '')
    if user and pwd:
        c = StudentInfo.objects.filter(stu_name=user,stu_pwd=pwd).count()#获取models里studentinfo类对象的值
        if c >= 1:
            return HttpResponse("登陆成功")
        else:
            return HttpResponse("用户名或密码错误")
    else:
        return HttpResponse("用户名或密码为空")
    # return render(request, 'index.html')

def toregister_view(request):
    return render(request, 'register.html')

def register_view(request):
    user = request.POST.get("user", '')
    pwd = request.POST.get("pwd", '')
    confirm_pwd = request.POST.get("confirm_pwd", '')
    email = request.POST.get("email", '')
    course = request.POST.get("course", '')
    if user and pwd and confirm_pwd and email and course:
        c = StudentInfo.objects.filter(stu_name=user).count()
        if c:
            return HttpResponse("用户名已存在")
        elif pwd != confirm_pwd:
            return HttpResponse("密码不一致")
        else:
            stu = StudentInfo(stu_id=id,stu_name=user,stu_pwd=pwd,stu_email=email,stu_course=course)
            stu.save()
            return HttpResponse("注册成功")
    else:
        return HttpResponse("请补全信息")