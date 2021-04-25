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
            drop_link = './' + user + '/drop/'
            add_link = './' + user + '/add/'
            return render(request, 'studentindex0.html', context={'student': student, 'link':link, 'drop_link':drop_link, 'add_link':add_link})
        elif c1 >= 1:
            for student in StudentInfo.objects.all():
                if student.stu_name == user:
                    break
            link = link + user
            update_link = '../index/' + user + '/update/'
            return render(request, 'teacherindex0.html', context={'teacher': student, 'link':link, 'update_link':update_link})
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
    if student.stu_role == '1':
        return render(request, 'teacherindex.html', context={'teacher': student, 'link':link})
    else:
        return render(request, 'studentindex.html', context={'student': student, 'link':link})

# def teacher_view(request, user_name):
#     for student in StudentInfo.objects.all():
#         if student.stu_name == user_name:
#             break
#     link = '../../torewriteinfo/' + user_name + '/'
#     return render(request, 'teacherindex.html', context={'teacher': student, 'link': link})

def drop_view(request, user_name):
    for user in StudentInfo.objects.all():
        if user.stu_name == user_name:
            break
    courses_ids = user.stu_course.split(',')
    courses = []
    for course in CourseInfo.objects.all():
        if course.course_id in courses_ids:
            courses.append(course)
    return render(request, 'drop.html', context={'user':user, 'courses':courses})

def add_view(request, user_name):
    for user in StudentInfo.objects.all():
        if user.stu_name == user_name:
            break
    courses_ids = user.stu_course.split(',')
    courses = []
    for course in CourseInfo.objects.all():
        if course.course_id not in courses_ids:
            courses.append(course)
    return render(request, 'add.html', context={'user': user, 'courses': courses})

def Toadd_view(request, user_name):
    course_id = request.POST.get("course",'')
    if course_id:
        for user in StudentInfo.objects.all():
            if user.stu_name == user_name:
                break
        stu_id = user.stu_id
        stu_name = user.stu_name
        pwd = user.stu_pwd
        role = user.stu_role
        email = user.stu_email
        course = user.stu_course
        StudentInfo.objects.get(stu_name=stu_name).delete()
        new_stu_course = course + ',' + course_id
        stu = StudentInfo(stu_id=stu_id, stu_name=stu_name, stu_pwd=pwd, stu_email=email, stu_role=role,
                              stu_course=new_stu_course)
        stu.save()
    return render(request,'finish_add.html',context={'course':course_id})

def Todrop_view(request, user_name):
    course_id = request.POST.get("course",'')
    if course_id:
        for user in StudentInfo.objects.all():
            if user.stu_name == user_name:
                break
        stu_id = user.stu_id
        stu_name = user.stu_name
        pwd = user.stu_pwd
        role = user.stu_role
        email = user.stu_email
        course = user.stu_course
        StudentInfo.objects.get(stu_name=stu_name).delete()
        courses = course.split(',')
        courses.remove(course_id)
        new_stu_course = ''
        for c in courses:
            new_stu_course = new_stu_course + c + ','
        new_stu_course = new_stu_course[:-1]
        stu = StudentInfo(stu_id=stu_id, stu_name=stu_name, stu_pwd=pwd, stu_email=email, stu_role=role,
                              stu_course=new_stu_course)
        stu.save()
    return render(request,'finish_drop.html',context={'course':course_id})

def update_view(request, user_name):
    for user in StudentInfo.objects.all():
        if user.stu_name == user_name:
            break
    course = user.stu_course
    marks = []
    for mark in Studentmark.objects.all():
        if mark.course_id == course:
            marks.append(mark)
    return render(request, "update_accdemic_record.html",context={'marks':marks})

def Toupdate_view(request, user_name):
    for user in StudentInfo.objects.all():
        if user.stu_name == user_name:
            break
    course = user.stu_course
    for mark in Studentmark.objects.all():
        if mark.course_id == course:
            a_1 = request.POST.get(mark.stu_name + "a1", '')
            a_2 = request.POST.get(mark.stu_name + "a2", '')
            a_3 = request.POST.get(mark.stu_name + "a3", '')
            a_4 = request.POST.get(mark.stu_name + "a4", '')
            a_5 = request.POST.get(mark.stu_name + "a5", '')
            a_6 = request.POST.get(mark.stu_name + "a6", '')
            flag1,flag2,flag3,flag4,flag5,flag6 = 0,0,0,0,0,0
            if not a_1:
                a_1 = '0'
            if not a_2:
                a_2 = '0'
            if not a_3:
                a_3 = '0'
            if not a_4:
                a_4 = '0'
            if not a_5:
                a_5 = '0'
            if not a_6:
                a_6 = '0'
            if a_1 != mark.assignment_1:
                flag1 = 1
            if a_2 != mark.assignment_2:
                flag2 = 1
            if a_3 != mark.assignment_3:
                flag3 = 1
            if a_4 != mark.assignment_4:
                flag4 = 1
            if a_5 != mark.assignment_5:
                flag5 = 1
            if a_6 != mark.assignment_6:
                flag6 = 1
            if flag1 or flag2 or flag3 or flag4 or flag5 or flag6:
                mark_id = mark.mark_id
                stu_name = mark.stu_name
                stu_id = mark.stu_id
                Studentmark.objects.get(mark_id=mark_id).delete()
                new_mark = Studentmark(mark_id=mark_id,stu_id=stu_id,stu_name=stu_name,course_id=course,assignment_1=a_1,assignment_2=a_2,assignment_3=a_3,assignment_4=a_4,assignment_5=a_5,assignment_6=a_6)
                new_mark.save()

    return render(request, 'finish_update.html', context={'course':course})
