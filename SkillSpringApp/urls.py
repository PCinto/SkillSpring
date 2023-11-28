from django.contrib import admin
from django.urls import path
from SkillSpringApp import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.register, name='register'),
    path('login/', views.login, name='login'),

    path('index', views.index, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('courses/', views.courses, name='courses'),
    path('courses-details/', views.courses_details, name='courses-details'),
    path('events/', views.events, name='events'),
    path('pricing/', views.pricing, name='pricing'),
    path('trainers/', views.trainers, name='trainers'),
    path('pay/', views.pay, name='pay'),

    path('show/', views.show, name='show'),
    path('joined/', views.joined, name='joined'),

    path('delete/<int:id>', views.delete),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),

    path('software/', views.software, name='SoftwareEngineering'),
    path('datascience/', views.datascience, name='datascience'),
    path('cybersecurity/', views.cybersecurity, name='cybersecurity'),
    path('networking/', views.networking, name='networking'),
    path('GraphicDesign/', views.GraphicDesign, name='GraphicDesign'),
    path('dataanalysis/', views.dataanalysis, name='dataanalysis'),

    path('token/', views.token, name='token'),
    path('stk/', views.stk, name='stk'),
]
