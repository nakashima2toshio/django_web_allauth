# django_web_allauth/urls.py
from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

# site-packages\allauth\accounts\urls.py
# http://127.0.0.1:8000/accounts/login/
# http://127.0.0.1:8000/accounts/logout/
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='home.html'), name='home'),
    path('accounts/', include('allauth.urls')),
]
