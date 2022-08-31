"""chisp URL Configuration

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

from mainApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', views.index, name='index'),
    path('component/<pk>', views.ViewComponent.as_view(), name='component.view'),
    path('insert/', views.CreateComponent.as_view(), name="component.insert"),
    path('list/', views.ComponentListView.as_view(), name="component.list"),
    path('search/', views.SearchComponent.as_view(), name="component.search_results"),
    path('edit/<pk>', views.UpdateComponent.as_view(), name="component.edit_component"),
    path('', views.index, name="home")
]
