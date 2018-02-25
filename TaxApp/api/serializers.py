from rest_framework import serializers
from TaxApp.api import models


def get_fields(model_class):
    '''Gets a list of field names of the given model_class'''
    return tuple(field.name for field in model_class._meta.get_fields())


class CountrySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Country
        fields = get_fields(models.Country)


class StateSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.State
        fields = get_fields(models.State)


class LgaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Lga
        fields = get_fields(models.Lga)


class TaxPayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.TaxPayer
        exclude = ('user',)


class CorporateTaxPayerSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CorporateTaxPayer
        exclude = ('user',)


class ResidentialAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ResidentialAddress
        fields = get_fields(models.ResidentialAddress)


class CompanyAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CompanyAddress
        fields = get_fields(models.CompanyAddress)


class BiometricSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Biometric
        fields = get_fields(models.Biometric)


class IdentificationDocumentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.IdentificationDocument
        fields = get_fields(models.IdentificationDocument)
