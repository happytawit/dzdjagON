from django.db import models

class Partner(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=250, blank=True)
    def __unicode__(self):
        return self.name
