from django.urls import reverse_lazy
from django.views import generic

from . import forms
from . import models


class LibraryListView(generic.ListView):
    model = models.Library
    form_class = forms.LibraryForm


class LibraryCreateView(generic.CreateView):
    model = models.Library
    form_class = forms.LibraryForm


class LibraryDetailView(generic.DetailView):
    model = models.Library
    form_class = forms.LibraryForm


class LibraryUpdateView(generic.UpdateView):
    model = models.Library
    form_class = forms.LibraryForm
    pk_url_kwarg = "pk"


class LibraryDeleteView(generic.DeleteView):
    model = models.Library
    success_url = reverse_lazy("library_list")


class ResourceListView(generic.ListView):
    model = models.Resource
    form_class = forms.ResourceForm


class ResourceCreateView(generic.CreateView):
    model = models.Resource
    form_class = forms.ResourceForm


class ResourceDetailView(generic.DetailView):
    model = models.Resource
    form_class = forms.ResourceForm


class ResourceUpdateView(generic.UpdateView):
    model = models.Resource
    form_class = forms.ResourceForm
    pk_url_kwarg = "pk"


class ResourceDeleteView(generic.DeleteView):
    model = models.Resource
    success_url = reverse_lazy("resource_list")


class PermissionsListView(generic.ListView):
    model = models.Permissions
    form_class = forms.PermissionsForm


class PermissionsCreateView(generic.CreateView):
    model = models.Permissions
    form_class = forms.PermissionsForm


class PermissionsDetailView(generic.DetailView):
    model = models.Permissions
    form_class = forms.PermissionsForm


class PermissionsUpdateView(generic.UpdateView):
    model = models.Permissions
    form_class = forms.PermissionsForm
    pk_url_kwarg = "pk"


class PermissionsDeleteView(generic.DeleteView):
    model = models.Permissions
    success_url = reverse_lazy("permissions_list")
