from django.contrib import admin
from .models import Suburb

# Register your models here.


class SuburbAdmin(admin.ModelAdmin):
    list_display = (
        "suburb",
        "population",
    )

    ordering = ("suburb",)

admin.site.register(Suburb, SuburbAdmin)
