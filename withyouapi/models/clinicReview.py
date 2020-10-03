from django.db import models
from django.contrib.auth.models import User


class ClinicReview(models.Model):
    
    clinic_id = models.ForeignKey('Clinic', max_length=50, on_delete=models.DO_NOTHING)
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    rating = models.IntegerField()
    review = models.CharField(max_length=3000)
    
    class Meta:
        ordering = ("clinic_id", )
        verbose_name = ("clinic review")
        verbose_name_plural = ("clinic reviews")