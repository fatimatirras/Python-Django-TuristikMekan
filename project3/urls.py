"""project3 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from home import views

urlpatterns = [

    path('', include('home.urls')),
    path('home/', include('home.urls')),
    path('place/', include('place.urls')),
    path('user/', include('user.urls')),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('content/', include('content.urls')),
    path('contact/', views.contact, name='contact'),
    path('aboutus/', views.aboutus, name='aboutus'),
    path('references/', views.references, name='references'),
    path('category/<int:id>/<slug:slug>/', views.category_places, name='category_places'),

    path('category/<int:id>/<slug:slug>/', views.category_userplaces, name='category_userplaces'),

    path('place/<int:id>/<slug:slug>/', views.place_detail, name='place_detail'),
    path('search/', views.place_search, name='place_search'),
    path('search_auto/', views.place_search_auto, name='place_search_auto'),
    path('logout/', views.logout_view, name='logout_view'),
    path('login/', views.login_view, name='login_view'),
    path('signup/', views.signup_view, name='signup_view'),
    path('sss/', views.faq, name='faq'),

    path('content/<int:id>/<slug:slug>/', views.contentdetail, name='contentdetail'),
    path('menu/<int:id>', views.menu, name='menu'),




]

if settings.DEBUG:  #new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)