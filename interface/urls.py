
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('services/', views.services, name='services'),
     path('contact/', views.contact, name='contact'),
     path('resume/', views.resume, name='resume'),
     path('contact_success/', views.contact_success, name='contact_success'),
    
]+static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT)


