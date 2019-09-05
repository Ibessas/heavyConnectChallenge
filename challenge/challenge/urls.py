"""challenge URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
#from core.views import ReportViewSet
#from core.views import ReportResponseViewSet
#from core.views import UserViewSet
from core import views
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns


router = routers.DefaultRouter()

#router.register(r'reports', ReportViewSet)
#router.register(r'response', ReportResponseViewSet)
#router.register(r'user', UserViewSet)

urlpatterns = [
    url('admin/', admin.site.urls),
    url('reports/', views.ReportList.as_view()),
    url('response/', views.ResponseList.as_view()),
    
    #path('', include(router.urls)),
    #path('api-auth/', include('rest_framework.urls'))
]

urlpatterns = format_suffix_patterns(urlpatterns)
