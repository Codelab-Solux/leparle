from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('courses/', courses, name='courses'),
    path('courses/<str:pk>/', course_details, name='course'),
    path('sectors/', sectors, name='sectors'),
    path('sectors/<str:pk>/', sector_details, name='sector'),
    path('blog/', blog, name='blog'),
    path('blog/<str:pk>/', blogpost, name='blogpost'),
    path('dashboard/', dashboard, name='dashboard'),

]
