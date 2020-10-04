from django.db import models

class Form(models.Model):
    
    member = models.ForeignKey('Member', on_delete=models.DO_NOTHING)
    form_data = models.JSONField()
    form_type = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=False)
    
    
    class Meta:
        verbose_name = ("form")
        verbose_name_plural = ("forms")
