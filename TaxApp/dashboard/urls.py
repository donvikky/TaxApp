from django.urls import path
from django.views.generic import RedirectView
from TaxApp.dashboard import views

urlpatterns = [
    path('', RedirectView.as_view(url='overview/', permanent=True)),
    path('overview/', views.overview, name='overview'),
    path('user/', views.user_profile, name='user_profile'),
    path('enrollment/', RedirectView.as_view(url='individual/', permanent=True)),
    path('enrollment/individual/', views.TaxPayerList.as_view(), name='individual_list'),
    path('enrollment/individual/create', views.TaxPayerCreate.as_view(), name='individual_create'),
    path('enrollment/individual/<int:pk>', views.TaxPayerDetail.as_view(), name='individual_detail'),
    path('enrollment/corporate/', views.CorporateTaxPayerList.as_view(), name='corporate_list'),
    path('enrollment/corporate/create', views.CorporateTaxPayerCreate.as_view(), name='corporate_create'),
    path('enrollment/corporate/<int:pk>', views.CorporateTaxPayerDetail.as_view(), name='corporate_detail'),
]
