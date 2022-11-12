from django import forms

from scdn.models import Library
from scdn.models import Resource
from . import models


class LibraryForm(forms.ModelForm):
    class Meta:
        model = models.Library
        fields = [
            "title",
            "description",
        ]

    def __init__(self, *args, **kwargs):
        super(LibraryForm, self).__init__(*args, **kwargs)


class ResourceForm(forms.ModelForm):
    class Meta:
        model = models.Resource
        fields = [
            "version",
            "title",
            "file",
            "library",
            "parent",
        ]

    def __init__(self, *args, **kwargs):
        super(ResourceForm, self).__init__(*args, **kwargs)
        self.fields["library"].queryset = Library.objects.all()
        self.fields["parent"].queryset = Resource.objects.all()


class PermissionsForm(forms.ModelForm):
    class Meta:
        model = models.Permissions
        fields = [
            "regex",
            "library",
            "resource",
        ]

    def __init__(self, *args, **kwargs):
        super(PermissionsForm, self).__init__(*args, **kwargs)
        self.fields["library"].queryset = Library.objects.all()
        self.fields["resource"].queryset = Resource.objects.all()
