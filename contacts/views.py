# -*- coding: utf-8 -*-
from django.shortcuts import render
from .models import Contact

def contacts(request):
    contact_list = Contact.objects.filter(name__startswith="Владимир")
    context = {'contacts':contact_list}
    return render(request, 'contacts/contacts.html', context)
    