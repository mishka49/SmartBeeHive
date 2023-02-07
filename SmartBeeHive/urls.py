"""SmartBeeHive URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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

from SmartBeeHive import settings
from hives.views import *

urlpatterns = [
    path('', view_home_page),
    path('admin/', admin.site.urls),
    path('service/', view_service_page),
    path('subscription/', view_subscription_page),
    path('add_subscription/', view_addsubscription_page),
    path('subscription_delete_conf/', view_delete_subscription),
    path('subscription_delete/', delete_subscription),
    path('send_subscription_form/', get_form_subscription),
    path('hive/', view_hive_page),
    path('report/', view_report_page),
    path('download/', download_file),
    path('card/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]
