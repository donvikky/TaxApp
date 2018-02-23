from django.core.exceptions import ImproperlyConfigured
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.contrib import messages
from TaxApp.api import models
from TaxApp.dashboard import forms


def overview(request):
    return render(request, 'dashboard/overview.html')


def userprofile(request):
    user = request.user
    form = forms.UserEditForm(user)

    if request.POST:
        form = forms.UserEditForm(user, request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, 'User Profile Updated!', extra_tags='alert-success')
            return redirect(request.path)

    return render(request, 'dashboard/userprofile.html', {'form': form, 'user': user})


class EnrollmentView(CreateView):

    @property
    def address_form_class(self):
        '''Get the applicable address form class for this instance'''
        if self.model is models.TaxPayer:
            return forms.ResidentialAddressForm
        elif self.model is models.CorporateTaxPayer:
            return forms.CompanyAddressForm
        else:
            error_message = (
                'address_form_class must be one of '
                '[ResidentialAddressForm, CompanyAddressForm]'
            )
            raise ImproperlyConfigured(error_message)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        address_form = self.address_form_class(self.request.POST)
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

        return redirect(self.success_url)


class TaxPayerCreate(EnrollmentView):
    model = models.TaxPayer
    fields = (
        'surname', 'first_name', 'other_name', 'marital_status', 'gender', 'dob',
        'lga_of_origin', 'state_of_origin', 'nationality', 'tax_payer_company',
        'occupation', 'employment_status', 'phone', 'email',
    )
    template_name = 'dashboard/individual/create.html'
    success_url = '/dashboard/enrollment/individual/'


class CorporateTaxPayerCreate(EnrollmentView):
    model = models.CorporateTaxPayer
    fields = (
        'name', 'trade_name', 'phone', 'email', 'company_size', 'ownership_type',
        'reg_status', 'reg_date', 'start_date', 'reg_no', 'line_of_business',
        'sector', 'contact_name'
    )
    template_name = 'dashboard/corporate/create.html'
    success_url = '/dashboard/enrollment/corporate/'


class PaginatedListView(ListView):
    paginate_by = 20

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_paginated'] = True
        return context

    def get_paginate_by(self, queryset):
        '''Get the number of items per page from query string'''
        return self.request.GET.get('items', self.paginate_by)


class TaxPayerList(PaginatedListView):
    model = models.TaxPayer
    context_object_name = 'tax_payers'
    template_name = 'dashboard/individual/list.html'


class CorporateTaxPayerList(PaginatedListView):
    model = models.CorporateTaxPayer
    context_object_name = 'tax_payers'
    template_name = 'dashboard/corporate/list.html'
