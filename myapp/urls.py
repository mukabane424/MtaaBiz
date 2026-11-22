
from django.contrib import admin
from django.urls import path
from myapp import views
from django.shortcuts import redirect


urlpatterns = [
    
    path('admin/', admin.site.urls),

    path('error/', views.error, name='error'),

    path('details/', views.details, name='details'),

    path('blog/', views.blog, name='blog'),

    path('', views.index, name='index'),

    path('portfolio/', views.portfolio, name='portfolio'),

    path('contact/', views.contact, name='contact'),

    path('service/', views.service, name='service'),

    path('show/', views.show, name='show'),

    path('delete/<int:id>/', views.delete, name='delete'),

    path('edit/', lambda request: redirect('show')),

    path('edit/<int:id>/', views.edit, name='edit'),

    
]


   
