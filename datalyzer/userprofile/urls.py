from django.urls import path, include
from . import views
from django.contrib.auth import views as auth_views

app_name = 'userprofile'


urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('signin/', auth_views.LoginView.as_view(template_name='userprofile/signin.html'), name='signin'),
    path('signout/', auth_views.LogoutView.as_view(next_page='main:home'), name='signout')
]

