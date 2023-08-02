from django.urls import path
from . import views

# app_name="showroomapp"

urlpatterns = [
    path('', views.home, name='home'),
    path('brand/<int:brand_id>/', views.brand, name='brand'),
    path('team/', views.team, name='team'),
]