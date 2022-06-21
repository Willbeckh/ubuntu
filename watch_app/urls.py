from django.urls import path, include

# local imports
from .views import *
from watch_app import views

app_name = 'watch'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('profile/<int:pk>/update/', views.edit_user, name='edit_profile'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('post/', PostView.as_view(), name='post'),
    # path('facility/', FacilityView.as_view(), name='facility')
]
