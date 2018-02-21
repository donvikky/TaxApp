from django.core.exceptions import ImproperlyConfigured
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from TaxApp.api import models
from TaxApp.dashboard import forms


def overview(request):
    return render(request, 'dashboard/overview.html')


class EnrollmentView(CreateView):

    @property
    def address_form_class(self):
        '''Get the applicable address form class for this instance'''
        if type(self.model, models.TaxPayer):
            return forms.ResidentialAddressForm
        elif type(self.model, models.CorporateTaxPayer):
            return forms.CompanyAddressForm
        else:
            error_message = (
                'address_form_class must be one of '
                '[ResidentialAddressForm, CompanyAddressForm]'
            )
            raise ImproperlyConfigured(error_message)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        address_form = self.address_form_class()
        context['address_form'] = address_form

        return context

    def get_address_model(self):
        address_form = self.address_form_class(self.request.POST)
        address = address_form.save(commit=False)

        return address

    def form_valid(self, form):
        tax_payer = form.save()
        address = self.get_address_model()
        address.tax_payer = tax_payer
        address.save()

        return redirect(self.get_success_url())


class TaxPayerCreate(EnrollmentView):
    model = models.TaxPayer
    template_name = 'dashboard/individual/create.html'


class CorporateTaxPayerCreate(EnrollmentView):
    model = models.CorporateTaxPayer
    template_name = 'dashboard/corporate/create.html'


class TaxPayerList(ListView):
    model = models.TaxPayer
    context_object_name = 'tax_payers'
    template_name = 'dashboard/individual/list.html'


class CorporateTaxPayerList(ListView):
    model = models.CorporateTaxPayer
    context_object_name = 'tax_payers'
    template_name = 'dashboard/corporate/list.html'
