"""rainbow_felt_designs URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from home import views
from accounts import views as account_views
from products import views as product_views
from shopping import views as shopping_views
from paypal_store import views as paypal_views
from paypal.standard.ipn import urls as paypal_urls

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index_page, name='home'),
    url(r'^about/', views.about_page),

    # Auth URLS
    url(r'^register/', account_views.register, name='register'),
    url(r'^login/', account_views.login, name='login'),
    url(r'^logout', account_views.logout, name='logout'),
    url(r'^myaccount/', account_views.myaccount, name='myaccount'),

    # Product URLS
    url(r'^products/$', product_views.all_products, name='all_products'),
    url(r'^products/(?P<id>\d+)/$', product_views.product_view, name='product_view'),
    url(r'^customorder/$', product_views.custom_request, name='custom_request'),

    # Shopping Cart URLS    
    url(r'^shopping-cart/add/$', shopping_views.add, name='shopping-cart-add'),
    url(r'^shopping-cart/remove/$', shopping_views.remove, name='shopping-cart-remove'),
    url(r'^shopping-cart/show/$', shopping_views.show, name='shopping-cart-show'),

    # Paypal URLS
    url(r'^temp-complicated-url/', include(paypal_urls)),
    url(r'^paypal-return', paypal_views.paypal_return),
    url(r'^paypal-cancel', paypal_views.paypal_cancel),
]
