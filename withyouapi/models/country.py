from django.db import models

class Country(models.Model):
    
    name = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    
    class Meta:
        ordering = ("name", )
        verbose_name = ("country")
        verbose_name_plural = ("countries")