from django.contrib import admin
from . import models

admin.site.register([
    models.Country,
    models.State,
    models.Lga,
    models.Address,
    models.TaxPayer,
    models.CorporateTaxPayer,
])
