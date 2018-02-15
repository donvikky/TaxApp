from django.urls import path, include
from rest_framework.routers import DefaultRouter
from TaxApp.api import views


router = DefaultRouter()

router.register(r'individual', views.TaxPayerViewset)
router.register(r'corporate', views.CorporateTaxPayerViewset)
router.register(r'residential_addresses', views.ResidentialAddressViewset)
router.register(r'company_addresses', views.CompanyAddressViewset)

urlpatterns = [
    path(r'^auth/', include('rest_framework.urls')),
    path(r'^', include(router.urls)),
]
