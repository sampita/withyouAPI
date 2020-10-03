from django.db import models

class City(models.Model):
    
    name = models.CharField(max_length=50)
    country_id = models.ForeignKey('Country', on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    
    class Meta:
        ordering = ("name", )
        verbose_name = ("city")
        verbose_name_plural = ("cities")