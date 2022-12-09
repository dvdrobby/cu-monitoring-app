from django.contrib import admin

from .models import FormModel


class FormSlug(admin.ModelAdmin):
    readonly_fields=['form_slug']

admin.site.register(FormModel, FormSlug)
