from django.db import models

class Presentation(models.Model):
    name = models.CharField(max_length=150)
    description = models.CharField(max_length=250, blank=True)
    speaker = models.ForeignKey('speakers.Speaker')
    def __unicode__(self):
        return self.name
