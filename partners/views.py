from django.shortcuts import render
from .models import Partner
from .forms import AddPartner
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

def partners(request):
    partners_list = Partner.objects.all()
    context = {'partners':partners_list}
    return render(request, 'partners/partners.html', context)

def edit(request):
    form = AddPartner()
    return render(request, 'partners/edit.html', {'form':form})

def add(request):
    if request.method == 'POST':
        form = AddPartner(request.POST)
        if form.is_valid():
            p = Partner()
            p.name = form.cleaned_data['name']
            p.description = form.cleaned_data['description']
            p.save()
            return HttpResponseRedirect(reverse('partners:partners'))
    else:
        form = AddPartner()
    return render(request, 'partners/edit.html', {'form':form})
            
    