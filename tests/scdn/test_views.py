import pytest
import test_helpers

from django.urls import reverse


pytestmark = [pytest.mark.django_db]


def tests_Library_list_view(client):
    instance1 = test_helpers.create_library()
    instance2 = test_helpers.create_library()
    url = reverse("library_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Library_create_view(client):
    url = reverse("library_create")
    data = {
        "title": "text",
        "description": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Library_detail_view(client):
    instance = test_helpers.create_library()
    url = reverse("library_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Library_update_view(client):
    instance = test_helpers.create_library()
    url = reverse("library_update", args=[instance.pk, ])
    data = {
        "title": "text",
        "description": "text",
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Resource_list_view(client):
    instance1 = test_helpers.create_resource()
    instance2 = test_helpers.create_resource()
    url = reverse("resource_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Resource_create_view(client):
    library = test_helpers.create_library()
    parent = test_helpers.create_resource()
    url = reverse("resource_create")
    data = {
        "version": "text",
        "title": "text",
        "file": "aFile",
        "library": library.pk,
        "parent": parent.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Resource_detail_view(client):
    instance = test_helpers.create_resource()
    url = reverse("resource_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Resource_update_view(client):
    library = test_helpers.create_library()
    parent = test_helpers.create_resource()
    instance = test_helpers.create_resource()
    url = reverse("resource_update", args=[instance.pk, ])
    data = {
        "version": "text",
        "title": "text",
        "file": "aFile",
        "library": library.pk,
        "parent": parent.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Permissions_list_view(client):
    instance1 = test_helpers.create_permissions()
    instance2 = test_helpers.create_permissions()
    url = reverse("permissions_list")
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance1) in response.content.decode("utf-8")
    assert str(instance2) in response.content.decode("utf-8")


def tests_Permissions_create_view(client):
    library = test_helpers.create_library()
    resource = test_helpers.create_resource()
    url = reverse("permissions_create")
    data = {
        "allow_all": true,
        "regex": "text",
        "library": library.pk,
        "resource": resource.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302


def tests_Permissions_detail_view(client):
    instance = test_helpers.create_permissions()
    url = reverse("permissions_detail", args=[instance.pk, ])
    response = client.get(url)
    assert response.status_code == 200
    assert str(instance) in response.content.decode("utf-8")


def tests_Permissions_update_view(client):
    library = test_helpers.create_library()
    resource = test_helpers.create_resource()
    instance = test_helpers.create_permissions()
    url = reverse("permissions_update", args=[instance.pk, ])
    data = {
        "allow_all": true,
        "regex": "text",
        "library": library.pk,
        "resource": resource.pk,
    }
    response = client.post(url, data)
    assert response.status_code == 302
