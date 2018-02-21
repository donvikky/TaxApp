from rest_framework import viewsets
from TaxApp.api import models
from TaxApp.api import serializers
# from TaxApp.api import permissions


class CountryViewset(viewsets.ReadOnlyModelViewSet):
    queryset = models.Country.objects.all()
    serializer_class = serializers.CountrySerializer


class StateViewset(viewsets.ReadOnlyModelViewSet):
    queryset = models.State.objects.all()
    serializer_class = serializers.StateSerializer


class LgaViewset(viewsets.ReadOnlyModelViewSet):
    queryset = models.Lga.objects.all()
    serializer_class = serializers.LgaSerializer


class TaxPayerViewset(viewsets.ModelViewSet):
    queryset = models.TaxPayer.objects.all()
    serializer_class = serializers.TaxPayerSerializer

    def perform_create(self, serializer):
        # @todo: (1) create a new user (2) create TaxPayer setting user to this user
        # @todo: (3) send confirmation and password reset link
        # @todo: 1 and 2 above should be wrapped in a transaction
        serializer.save(user=self.request.user)


class CorporateTaxPayerViewset(viewsets.ModelViewSet):
    queryset = models.CorporateTaxPayer.objects.all()
    serializer_class = serializers.CorporateTaxPayerSerializer

    def perform_create(self, serializer):
        # @todo: see TaxPayerViewset above
        serializer.save(user=self.request.user)


class ResidentialAddressViewset(viewsets.ModelViewSet):
    queryset = models.ResidentialAddress.objects.all()
    serializer_class = serializers.ResidentialAddressSerializer
    filter_fields = ('tax_payer',)


class CompanyAddressViewset(viewsets.ModelViewSet):
    queryset = models.CompanyAddress.objects.all()
    serializer_class = serializers.CompanyAddressSerializer
    filter_fields = ('tax_payer',)
