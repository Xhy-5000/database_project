from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view),
    path('tologin/', views.toLogin_view),
    path('index/', views.Login_view),
    path('toregister/',views.toregister_view),
    path('register/',views.register_view),
]