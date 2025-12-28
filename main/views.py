from django.shortcuts import render
from .models import SiteSettings

def index_view(request):
    settings = SiteSettings.objects.first()
    context = {'settings': settings}
    return render(request, 'index.html', context)

def contact(request):
    return render(request, 'contacts.html')


