from django.db import models

class Contact(models.Model):
    name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=20, blank=True)
    email = models.EmailField(max_length=30, blank=True)
    address = models.CharField(max_length=150, blank=True)
    def __unicode__(self):
        return self.name
