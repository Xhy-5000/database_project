from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def toLogin_view(request):
    return render(request, 'login.html')

def Login_view(request):
    user = request.GET.get("user", '')
    pwd = request.GET.get("pwd", '')
    if user=="Andy Xia" and pwd=="andy123":
        return HttpResponse("登陆成功")
    else:
        return HttpResponse("用户名或密码错误")
    # return render(request, 'index.html')