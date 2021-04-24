from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view),
    path('tologin/', views.toLogin_view),
    # path('login/', views.Login_view),
    path('index/', views.Login_view),
    path('index/<str:link>/', views.index_view),
    path('index/<str:user_name>/add_and_drop/', views.add_and_drop_view),
    path('torewriteinfo/<str:link>/', views.toRewrite_view),
    path('rewriteinfo/<str:link>/', views.Rewrite_view),
    path('toregister/', views.toregister_view),
    path('register/', views.register_view),
    path('index/<str:user_name>/stu_showCourses/', views.stu_showCourses_view),
]