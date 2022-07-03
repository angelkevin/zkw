"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from views import plot
urlpatterns = [
    path('admin/', admin.site.urls),
    # path('views/', view.load),
    # path('login/', view.login),
    # path('signup/', view.signup),
    # path('signup_1/', view.singup_1),
    # path('bar/', plot.bar_show),
    # path('map/', plot.map_show),
    path('all/', plot.all_show),
]
