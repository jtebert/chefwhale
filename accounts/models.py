from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from userena.models import UserenaBaseProfile
from timezone_field import TimeZoneField


class UserProfile(UserenaBaseProfile):
    user = models.OneToOneField(User,
                                unique=True,
                                verbose_name=_('user'),
                                related_name='user_profile')
    timezone = TimeZoneField(default='America/New_York')
    PRIVACY_CHOICES = (
        ('public', _("Public")),
        ('private', _("Private")),
        ('secret', _("Secret"))
    )
    default_recipe_privacy = models.CharField(max_length=10, choices=PRIVACY_CHOICES, default='public')