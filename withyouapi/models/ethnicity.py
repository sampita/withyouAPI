from django.db import models

class Ethnicity(models.Model):
    
    name = models.CharField(max_length=50, null=True)
    
    class Meta:
        ordering = ("name", )
        verbose_name = ("ethnicity")
        verbose_name_plural = ("ethnicities")
        