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