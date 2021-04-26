from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view),
    path('tologin/', views.toLogin_view),
    # path('login/', views.Login_view),
    path('index/', views.Login_view),
    path('index/<str:link>/', views.index_view),
    path('index/<str:user_name>/drop/', views.drop_view),
    path('index/<str:user_name>/add/', views.add_view),
    path('index/<str:user_name>/toadd/', views.Toadd_view),
    path('index/<str:user_name>/todrop/', views.Todrop_view),
    # path('t_index/<str:user_name>/', views.teacher_view),
    path('index/<str:user_name>/update/', views.update_view),
    path('index/<str:user_name>/toupdate/', views.Toupdate_view),
    path('index/<str:user_name>/getqueryresult/', views.query_view),
    path('index/<str:user_name>/toquery/', views.Toquery_view),
    path('torewriteinfo/<str:link>/', views.toRewrite_view),
    path('rewriteinfo/<str:link>/', views.Rewrite_view),
    path('toregister/', views.toregister_view),
    path('register/', views.register_view),
    path('index/<str:user_name>/stu_showCourses/', views.stu_showCourses_view),
    path('index/<str:user_name>/show_courses/', views.show_courses_view),
    path('index/<str:user_name>/show_academic/', views.show_academic_view),
]