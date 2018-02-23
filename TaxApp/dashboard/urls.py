from django.urls import path
from django.views.generic import RedirectView
from TaxApp.dashboard import views

urlpatterns = [
    path('', RedirectView.as_view(url='overview/', permanent=True)),
    path('overview/', views.overview, name='dashboard.overview'),
    path('user/', views.userprofile, name='dashboard.userprofile'),
    path('enrollment/', RedirectView.as_view(url='individual/', permanent=True)),
    path('enrollment/individual/', views.TaxPayerList.as_view(), name='individual'),
    path('enrollment/corporate/', views.CorporateTaxPayerList.as_view()),
    path('enrollment/individual/create', views.TaxPayerCreate.as_view()),
    path('enrollment/corporate/create', views.CorporateTaxPayerCreate.as_view()),
]
