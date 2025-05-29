from django.urls import path
from .import views

urlpatterns = [

    path('entroll-confirmation/<str:uuid>/',views.EntrollConfirmationView.as_view(),name='entroll-confirmation')
]