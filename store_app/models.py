from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import gettext_lazy as _


User = get_user_model()


class Store(models.Model):
    user = models.ForeignKey(
        User, verbose_name=_("Store Owner"), on_delete=models.CASCADE
    )
    name = models.CharField(_("Store Name"), max_length=50, unique=True)

    def __str__(self) -> str:
        return self.name
