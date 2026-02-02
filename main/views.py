from django.shortcuts import render
from .models import CompanyInfo

def index_view(request):
    settings = CompanyInfo.objects.first()
    context = {'settings': settings}
    return render(request, 'index.html', context)

def contact(request):
    return render(request, 'contacts.html')


