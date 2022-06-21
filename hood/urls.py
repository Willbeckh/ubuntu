from django.urls import path , include
from hood import views

urlpatterns = [
    path('', views.Home , name="home"),
    path('login/', views.LoginPage , name="login"),
    path('register/', views.Register , name="register"),
    path('logout/', views.LogoutUser , name="logout"),
    path('profile/', views.profile , name="profile"),
    path('profile/update/', views.Update_Profile , name="update_profile"),

    path('business/', views.Businesses , name="business"),#businessroute

    path('profile/update/<int:pk>', views.edit_user, name='update'),


    path("post/save/", views.create_post, name="save_post"),# save post

    path("business/create/", views.create_business, name="create_business"), # create business
    path("search/", views.search_func , name="search"), # search




    # path("business/create/", views.create_business, name="create_business"), # create business












]
