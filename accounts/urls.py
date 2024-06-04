# accounts/urls.py
from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('login/', views.LoginView, name='login'),
    path('logout/', views.logout_view, name='logout'),
    # path('profile/', views.profile_view, name='profile'),
]
