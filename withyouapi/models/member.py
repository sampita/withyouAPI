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
    ethnicity_id = models.ForeignKey('Ethnicity', on_delete=models.DO_NOTHING)
    country_id = models.ForeignKey('Country', on_delete=models.DO_NOTHING)
    city_id = models.ForeignKey('City', on_delete=models.DO_NOTHING)
    member_type = models.ForeignKey('MemberType', on_delete=models.DO_NOTHING)
    # first_name, last_name, email, created_at, and is_active are all inherited from Django REST's built-in User

    class Meta:
        ordering = (F('user.date_joined').asc(nulls_last=True),)
        verbose_name = ("member")
        verbose_name_plural = ("members")
