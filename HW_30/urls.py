"""
URL configuration for HW_30 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from ads import views
from HW_30 import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.root),
    path('cat/', include('ads.urls.cat')),
    path('ad/', include('ads.urls.ad')),
    path('user/', include('users.urls.users')),
    path('location/', include('users.urls.locations')),
    path('select/', include('ads.urls.select')),
]



if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)