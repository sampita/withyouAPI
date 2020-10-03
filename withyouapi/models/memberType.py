from django.db import models

class MemberType(models.Model):
    
    category = models.CharField(max_length=50)
    
    class Meta:
        ordering = ("category", )
        verbose_name = ("member type")
        verbose_name_plural = ("member types")
