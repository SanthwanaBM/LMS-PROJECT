from django.urls import path
from .import views

urlpatterns = [

    path('student-register/',views.StudentRegistationView.as_view(),name='student-register')
]