from django.urls import path , include
from hood import views

urlpatterns = [
    path('', views.Home , name="home"),
    path('login/', views.LoginPage , name="login"),
    path('register/', views.Register , name="register"),
    path('logout/', views.LogoutUser , name="logout"),





]
