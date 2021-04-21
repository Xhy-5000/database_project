from django.urls import path
from . import views

urlpatterns = [
    path('', views.toLogin_view),
    path('index/', views.Login_view),
]