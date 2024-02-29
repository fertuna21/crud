from django.urls import path, include
from .import views

urlpatterns = [
    path('',views.teacher_form),
    path('list/',views.teacher_list)
]
