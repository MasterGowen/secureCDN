from django.contrib import admin
from django import forms

from . import models


class LibraryAdminForm(forms.ModelForm):

    class Meta:
        model = models.Library
        fields = "__all__"


class LibraryAdmin(admin.ModelAdmin):
    form = LibraryAdminForm
    list_display = [
        "title",
        "description",
    ]
    readonly_fields = [
        "title",
        "description",
    ]


class ResourceAdminForm(forms.ModelForm):

    class Meta:
        model = models.Resource
        fields = "__all__"


class ResourceAdmin(admin.ModelAdmin):
    form = ResourceAdminForm
    list_display = [
        "version",
        "title",
        "file",
    ]
    readonly_fields = [
        "version",
        "title",
        "file",
    ]


class PermissionsAdminForm(forms.ModelForm):

    class Meta:
        model = models.Permissions
        fields = "__all__"


class PermissionsAdmin(admin.ModelAdmin):
    form = PermissionsAdminForm
    list_display = [
        "allow_all",
        "regex",
    ]
    readonly_fields = [
        "allow_all",
        "regex",
    ]


admin.site.register(models.Library, LibraryAdmin)
admin.site.register(models.Resource, ResourceAdmin)
admin.site.register(models.Permissions, PermissionsAdmin)
