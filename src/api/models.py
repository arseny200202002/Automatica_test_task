from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

class Employee(models.Model):
    name = models.CharField(
        max_length=255, 
        verbose_name=_("имя")
    )
    phone_number = models.CharField(
        max_length=255, 
        null=False, 
        unique=True, 
        verbose_name=_("номер телефона")
    )

    def __str__(self):
        return self.name
    
    def is_authenticated(self):
        return True

    class Meta:
        db_table = "employee"
        verbose_name = _("Работник")
        verbose_name_plural = _("Работники")


class Shop(models.Model):
    name = models.CharField(
        max_length=255,
        null=False,
        unique=True,
        verbose_name=_("название")
    )
    employee = models.ForeignKey(
        to=Employee,
        on_delete=models.CASCADE,
        related_name='shops'
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = "shop"
        verbose_name = _("Торговая точка")
        verbose_name_plural = _("Торговые точки")


class Visit(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("время посещения")
    )
    latitude = models.FloatField(
        verbose_name=_("широта")
    )
    longitude = models.FloatField(
        verbose_name=_("долгота")
    )
    employee = models.ForeignKey(
        to=Employee,
        on_delete=models.CASCADE,
        related_name='visits'
    )
    shop = models.ForeignKey(
        to=Shop,
        on_delete=models.CASCADE,
        related_name='visits'
    )

    def __str__(self):
        return f'[{self.shop.name}] {self.employee.name}'


    class Meta:
        db_table = "shop_visit"
        verbose_name = _("Посещение")
        verbose_name_plural = _("Посещения")