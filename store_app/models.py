from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import RegexValidator
from django.utils.translation import gettext_lazy as _


User = get_user_model()


class StoreType(models.Model):
    name = models.CharField(_("Store Type"), max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name


class Store(models.Model):
    user = models.ForeignKey(
        User, verbose_name=_("Store Owner"), on_delete=models.CASCADE
    )
    type = models.ForeignKey(
        StoreType, verbose_name=_("Store Type"), on_delete=models.CASCADE
    )
    name = models.CharField(_("Store Name"), max_length=50, unique=True)
    description = models.TextField()
    address = models.CharField(
        _("Store Address"), max_length=255, blank=True, null=True
    )
    contact_number = models.CharField(
        max_length=50,
        validators=[
            RegexValidator(
                regex=r"^\+?(?:63)?(?:\d{10}|\d{11})$",
                message="Enter a valid phone number.",
            )
        ],
        blank=True,
        null=True,
    )
    open_from = models.TimeField(blank=True, null=True)
    open_to = models.TimeField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name
