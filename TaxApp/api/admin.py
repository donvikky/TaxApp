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


class SingleSerialAdmin(admin.ModelAdmin):
    readonly_fields = []

    def get_readonly_fields(self, request, obj=None):
        '''Make all field readonly'''
        readonly_fields = list(self.readonly_fields)
        if obj and hasattr(obj, '_meta'):
            readonly_fields.extend(field.name for field in obj._meta.fields)
            readonly_fields.extend(field.name for field in obj._meta.many_to_many)
        
        return readonly_fields

    def has_add_permission(self, request):
        '''Allow adding of only single instance'''
        if self.model.objects.count():
            return False
        
        return super().has_add_permission(request)

    def has_delete_permission(self, request, obj=None):
        return False


admin.site.register(models.TaxPayer, TaxPayerAdmin)
admin.site.register(models.CorporateTaxPayer, CorporateTaxPayerAdmin)
admin.site.register(models.Serial, SingleSerialAdmin)

admin.site.register([
    models.Country,
    models.State,
    models.Lga,
    models.ResidentialAddress,
    models.CompanyAddress,
])
