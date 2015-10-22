from django.db import models

class News(models.Model):
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    text = models.TextField()
    def __unicode__(self):
        return self.title
    class Meta:
        verbose_name_plural = "news"
