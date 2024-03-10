# myapp/urls.py
from django.urls import path
from . import views

app_name = 'oaa_app'

urlpatterns = [
    path('',views.home_view, name = 'home'),
    path('data/', views.data_view, name='data'),
    path('data_visualization/', views.data_visualization_view, name='data visualization'),
    # Add more URL patterns if needed
]
