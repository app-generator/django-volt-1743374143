# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Recipient(models.Model):

    #__Recipient_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.TextField(max_length=255, null=True, blank=True)

    #__Recipient_FIELDS__END

    class Meta:
        verbose_name        = _("Recipient")
        verbose_name_plural = _("Recipient")


class User(models.Model):

    #__User_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)

    #__User_FIELDS__END

    class Meta:
        verbose_name        = _("User")
        verbose_name_plural = _("User")


class Target(models.Model):

    #__Target_FIELDS__
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipient = models.ForeignKey(Recipient, on_delete=models.CASCADE)
    target_amount = models.IntegerField(null=True, blank=True)
    target_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    created_at = models.DateTimeField(blank=True, null=True, default=timezone.now)

    #__Target_FIELDS__END

    class Meta:
        verbose_name        = _("Target")
        verbose_name_plural = _("Target")


class Givingentry(models.Model):

    #__Givingentry_FIELDS__
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    target = models.ForeignKey(Target, on_delete=models.CASCADE)
    amount = models.IntegerField(null=True, blank=True)
    entry_date = models.DateTimeField(blank=True, null=True, default=timezone.now)
    note = models.TextField(max_length=255, null=True, blank=True)
    name = models.CharField(max_length=255, null=True, blank=True)

    #__Givingentry_FIELDS__END

    class Meta:
        verbose_name        = _("Givingentry")
        verbose_name_plural = _("Givingentry")



#__MODELS__END
