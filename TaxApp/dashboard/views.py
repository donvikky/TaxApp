from django.shortcuts import render


def overview(request):
    return render(request, 'dashboard/overview.html')


def create_individual(request):
    return render(request, 'dashboard/individual/create.html')


def create_corporate(request):
    return render(request, 'dashboard/corporate/create.html')


def list_individual(request):
    return render(request, 'dashboard/individual/list.html')


def list_corporate(request):
    return render(request, 'dashboard/corporate/list.html')
