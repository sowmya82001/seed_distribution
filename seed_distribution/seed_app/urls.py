from django.urls import path
from . import views
from .views import dashboard, seeds_view, farmers_view, distributions_view
from .views import contact


urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('', dashboard, name='dashboard'),
    path('seeds/', seeds_view, name='seeds'),
    path('farmers/', farmers_view, name='farmers'),
    path('distributions/', distributions_view, name='distributions'),
    path('contact/', contact, name='contact'),
]
