from django.urls import path, include


# local imports
from .views import *
from watch_app import views

app_name = 'watch'
urlpatterns = [
    path ('', HomeView.as_view(), name='home'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('edit_profile/<int:pk>/', views.edit_user, name='edit_profile'),
]