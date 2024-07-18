from django.contrib import admin
from .models import (
    Employee,
    Shop,
    Visit
)


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    search_fields = ['name']


@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    search_fields = ['name']


@admin.register(Visit)
class VisitAdmin(admin.ModelAdmin):
    search_fields = ['employee__name', 'shop__name']

