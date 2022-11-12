from django import forms
from django.contrib import admin
from nested_inline.admin import NestedModelAdmin, NestedTabularInline
from versionfield import VersionField
from .widgets import VersionWidget

from . import models


class ResourcePermissionsAdminInline(NestedTabularInline):
    extra = 0
    model = models.Permissions
    fk_name = 'resource'
    fields = ('regex',)


class LibraryPermissionsAdminInline(NestedTabularInline):
    extra = 0
    model = models.Permissions
    fk_name = 'library'


class ResourceAdminInline(NestedTabularInline):
    extra = 0
    model = models.Resource
    fields = ('title', 'version', 'file')
    inlines = (ResourcePermissionsAdminInline,)
    fk_name = 'library'
    formfield_overrides = {
        VersionField: {'widget': VersionWidget},
    }


class LibraryAdminForm(forms.ModelForm):
    class Meta:
        model = models.Library
        fields = '__all__'


@admin.register(models.Library)
class LibraryAdmin(NestedModelAdmin):
    form = LibraryAdminForm
    inlines = (ResourceAdminInline, LibraryPermissionsAdminInline)
    search_fields = ('title',)
    autocomplete_fields = ('parent',)
    list_display = [
        'title',
        'description',
        'version'
    ]


class ResourceAdminForm(forms.ModelForm):
    class Meta:
        model = models.Resource
        fields = '__all__'


@admin.register(models.Resource)
class ResourceAdmin(NestedModelAdmin):
    form = ResourceAdminForm
    inlines = [ResourcePermissionsAdminInline]
    list_display = [
        'version',
        'title',
        'file',
    ]


class PermissionsAdminForm(forms.ModelForm):
    class Meta:
        model = models.Permissions
        fields = '__all__'


@admin.register(models.Permissions)
class PermissionsAdmin(admin.ModelAdmin):
    form = PermissionsAdminForm
    list_display = [
        'regex',
    ]
