import random
import string

from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import Group
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType

from scdn import models as scdn_models


def random_string(length=10):
    # Create a random string of length length
    letters = string.ascii_lowercase
    return "".join(random.choice(letters) for i in range(length))


def create_User(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return User.objects.create(**defaults)


def create_AbstractUser(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return AbstractUser.objects.create(**defaults)


def create_AbstractBaseUser(**kwargs):
    defaults = {
        "username": "%s_username" % random_string(5),
        "email": "%s_username@tempurl.com" % random_string(5),
    }
    defaults.update(**kwargs)
    return AbstractBaseUser.objects.create(**defaults)


def create_Group(**kwargs):
    defaults = {
        "name": "%s_group" % random_string(5),
    }
    defaults.update(**kwargs)
    return Group.objects.create(**defaults)


def create_ContentType(**kwargs):
    defaults = {
    }
    defaults.update(**kwargs)
    return ContentType.objects.create(**defaults)


def create_library(**kwargs):
    defaults = {}
    defaults["title"] = ""
    defaults["description"] = ""
    defaults.update(**kwargs)
    return scdn_models.Library.objects.create(**defaults)


def create_resource(**kwargs):
    defaults = {}
    defaults["version"] = ""
    defaults["title"] = ""
    defaults["file"] = ""
    if "library" not in kwargs:
        defaults["library"] = create_library()
    if "parent" not in kwargs:
        defaults["parent"] = create_resource()
    defaults.update(**kwargs)
    return scdn_models.Resource.objects.create(**defaults)


def create_permissions(**kwargs):
    defaults = {}
    defaults["allow_all"] = ""
    defaults["regex"] = ""
    if "library" not in kwargs:
        defaults["library"] = create_library()
    if "resource" not in kwargs:
        defaults["resource"] = create_resource()
    defaults.update(**kwargs)
    return scdn_models.Permissions.objects.create(**defaults)