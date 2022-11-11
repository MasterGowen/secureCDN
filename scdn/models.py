from django.db import models
from django.urls import reverse
from versionfield import VersionField


class Library(models.Model):
    title = models.CharField(max_length=30)
    description = models.TextField(default="", blank=True)

    class Meta:
        verbose_name = 'library'
        verbose_name_plural = 'libraries'

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse("library_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("library_update", args=(self.pk,))


class Resource(models.Model):
    # Relationships
    library = models.ForeignKey("scdn.Library",  related_name='resources', on_delete=models.CASCADE)
    parent = models.ForeignKey("self", blank=True, null=True, on_delete=models.SET_NULL)

    # Fields
    version = VersionField()
    title = models.CharField(max_length=30)
    file = models.FileField(upload_to="upload/files/")

    class Meta:
        verbose_name = 'resource'
        verbose_name_plural = 'resources'

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return reverse("resource_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("resource_update", args=(self.pk,))


class Permissions(models.Model):
    # Relationships
    library = models.ForeignKey("scdn.Library", on_delete=models.CASCADE)
    resource = models.ForeignKey("scdn.Resource", on_delete=models.CASCADE)

    # Fields
    allow_all = models.BooleanField(default=False)
    regex = models.CharField(max_length=64)

    class Meta:
        verbose_name = 'permission'
        verbose_name_plural = 'permissions'

    def __str__(self):
        if self.library:
            return f"{self.library} {self.regex}"
        elif self.resource:
            return f"{self.resource} {self.regex}"

    def get_absolute_url(self):
        return reverse("permissions_detail", args=(self.pk,))

    def get_update_url(self):
        return reverse("permissions_update", args=(self.pk,))
