from django.urls import path , include
from hood import views

urlpatterns = [
    path('', views.Home , name="home"),
    path('login/', views.LoginPage , name="login"),
    path('register/', views.Register , name="register"),
    path('logout/', views.LogoutUser , name="logout"),
    path('profile/', views.profile , name="profile"),
    path('business/', views.Business , name="business"),

    path('profile/update/<int:pk>', views.edit_user, name='update'),









]
