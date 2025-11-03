from django.urls import path
from . import views


urlpatterns = [
    path('home/', views.home, name='home'),
    path('house/', views.house, name='house')
]