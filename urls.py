from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('home',views.home,name='home-page'),
    path('about',views.about,name='about-page'),
    path('work',views.work,name='work-page'),
    path('contact',views.Contact,name='contact-page'),
]
