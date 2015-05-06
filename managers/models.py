from django.db import models

class Manager(models.Model):
    name = models.CharField(max_length=150)
    title = models.CharField(max_length=150)
    def __unicode__(self):
        return self.name
