"""boohissbot URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from stocktrader.views import home_view, stock_search_view, stock_info_view, save_stock_view, stock_detail_view

urlpatterns = [
    path('', home_view, name='home'),
    path('stock-search/', stock_search_view, name='stock_search'),
    path('stock-info/', stock_info_view, name='stock_info'),
    path('save-stock/', save_stock_view, name='save_stock'),
    path('stock-details/', stock_detail_view, name='stock_details'),
    path('admin/', admin.site.urls),
]
