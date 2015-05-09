from django.shortcuts import render, render_to_response
from .models import Partner
from .forms import AddPartner
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def partners(request):
    partners_list = Partner.objects.all()
    paginator = Paginator(partners_list, 2)
    page = request.GET.get('page')
    try:
        partners_pag = paginator.page(page)
    except PageNotAnInteger:
        partners_pag = paginator.page(1)
    except EmptyPage:
        partners_pag = paginator.page(paginator.num_pages)
    context = {'partners':partners_list,
               'pag':partners_pag,
              }
    return render_to_response('partners/partners.html', context)

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
            
    