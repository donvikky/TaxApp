from django.forms import modelform_factory
from TaxApp.api import models

ResidentialAddressForm = modelform_factory(
    models.ResidentialAddress, exclude=('tax_payer',))

CompanyAddressForm = modelform_factory(
    models.CompanyAddress, exclude=('tax_payer',))
