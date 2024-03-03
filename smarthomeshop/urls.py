"""
URL configuration for smarthomeshop project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from shop.views import main_page, about, shop, contact
from orders.views import show, checkout
from accounts.views import login, logout
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('main/', main_page, name="main"),
    path('about/', about, name="about"),
    path('shop/', shop, name="shop"),
    path('show/', show, name="show"),
    path('checkout/', checkout, name="checkout"),
    path('login/', login, name="login"),  # czy to usunąć
    path('logout/', logout, name="logout"),
    path('contact/', contact, name="contact"),
    path('login/', auth_views.LoginView.as_view()),
    path('loout/', auth_views.LogoutView.as_view()),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
