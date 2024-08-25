from django.urls import path
from .import views
urlpatterns = [
    path('skill/',views.skill,name='skill'),
    path('certificate/',views.certificate, name='certificate'),
    path('resume/',views.resume, name='resume'),
    path('projects/',views.projects, name='projects')
]
