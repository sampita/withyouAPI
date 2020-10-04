from django.db import models
from django.db.models import F
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Member(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)
    birth_date = models.DateField()
    last_screening = models.DateField(null=True)
    diagnosis_date = models.DateField(null=True)
    ethnicity = models.ForeignKey('Ethnicity', on_delete=models.DO_NOTHING)
    street_address = models.CharField(max_length=50, null=True)
    street_address_2 = models.CharField(max_length=50, null=True)
    postal_code = models.CharField(max_length=25, null=True)
    country = models.ForeignKey('Country', on_delete=models.DO_NOTHING)
    city = models.ForeignKey('City', on_delete=models.DO_NOTHING)
    member_type = models.ForeignKey('MemberType', on_delete=models.DO_NOTHING)
    # first_name, last_name, email, created_at, and is_active are all inherited from Django REST's built-in User

    class Meta:
        ordering = ('user',)
        verbose_name = ("member")
        verbose_name_plural = ("members")
