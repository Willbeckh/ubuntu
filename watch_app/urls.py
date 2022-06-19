from django.urls import path, include


# local imports
from .views import *

app_name = 'watch'
urlpatterns = [
    path ('', HomeView.as_view(), name='home'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
]