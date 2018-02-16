from django.contrib import admin
from TaxApp.api import models


class ResidentialAddressInline(admin.TabularInline):
    model = models.ResidentialAddress


class CompanyAddressInline(admin.TabularInline):
    model = models.CompanyAddress


class TaxPayerAdmin(admin.ModelAdmin):
    inlines = [ResidentialAddressInline]


class CorporateTaxPayerAdmin(admin.ModelAdmin):
    inlines = [CompanyAddressInline]


admin.site.register(models.TaxPayer, TaxPayerAdmin)
admin.site.register(models.CorporateTaxPayer, CorporateTaxPayerAdmin)

admin.site.register([
    models.Country,
    models.State,
    models.Lga,
    models.ResidentialAddress,
    models.CompanyAddress,
])
