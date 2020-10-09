from django.db import models
from django.contrib.auth.models import User

class Clinic(models.Model):
    
    name = models.CharField(max_length=50)
    street_address = models.CharField(max_length=80)
    street_address_2 = models.CharField(max_length=80)
    city = models.ForeignKey('City', on_delete=models.DO_NOTHING)
    country = models.ForeignKey('Country', on_delete=models.DO_NOTHING)
    postal_code = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    created_by = models.ForeignKey(User, related_name="created_by", on_delete=models.DO_NOTHING)
    updated_by = models.ForeignKey(User, related_name="updated_by", on_delete=models.DO_NOTHING)
    is_validated = models.BooleanField(default=False)
    
    class Meta:
        ordering = ("name", )
        verbose_name = ("clinic")
        verbose_name_plural = ("clinics")