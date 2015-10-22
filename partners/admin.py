from django.contrib import admin
from .models import Partner

class PartnerAdmin(admin.ModelAdmin):
    search_fields = ['name']

admin.site.register(Partner, PartnerAdmin)
