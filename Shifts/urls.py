from django.urls import path
from . import views

urlpatterns = [
    path('',views.shiftsview,name="createshifts"),
    path('getShift/',views.getShift)
]
