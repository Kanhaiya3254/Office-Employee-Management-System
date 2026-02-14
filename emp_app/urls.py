from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('all_emp/', views.all_emp, name='all_emp'),
    path('remove_emp/', views.remove_emp, name='remove_emp'),
    path('remove_emp/<int:emp_id>/', views.remove_emp, name='remove_emp'),
]
