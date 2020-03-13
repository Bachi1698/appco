from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('blog/', views.blog, name='blog'),
    path('feature/', views.feature, name='feature'),
    path('elements', views.elements, name='elements'),
    path('pricing', views.pricing, name='pricing'),
    path('services/', views.services, name='services'),
    path('single_blog/', views.single_blog, name='single-blog'),
    
    
]