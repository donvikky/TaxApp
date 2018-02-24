"""TaxApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.urls import include, path, re_path
from django.views.generic import RedirectView
from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from rest_framework.authtoken.views import obtain_auth_token
from TaxApp.dashboard import views

urlpatterns = [
    path('', RedirectView.as_view(url='/dashboard/overview/', permanent=True)),
    path('dashboard/', include('TaxApp.dashboard.urls')),
    path('accounts/login/', LoginView.as_view(), name='login'),
    path('accounts/logout/',
        LogoutView.as_view(next_page=settings.LOGIN_URL), name='logout'),
    path('api/', include('TaxApp.api.urls')),
    path('api-auth/', obtain_auth_token),
    path('admin/', admin.site.urls),
    re_path(
        '^fonts/(?P<path>.*)$',
        RedirectView.as_view(url=settings.STATIC_URL +
                             'fonts/%(path)s', permanent=True),
        name='fonts'
    )
]
