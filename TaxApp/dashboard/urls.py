from django.urls import path
from django.views.generic import RedirectView
from TaxApp.dashboard import views

urlpatterns = [
    path('overview/', views.overview, name='dashboard.overview'),
    path('enrollment/individual/', views.list_individual),
    path('enrollment/corporate/', views.list_corporate),
    path('enrollment/individual/create', views.create_individual),
    path('enrollment/corporate/create', views.create_corporate),
]
