# Generated by Django 4.1.3 on 2022-11-12 05:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scdn', '0002_alter_library_options_alter_permissions_options_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='permissions',
            name='allow_all',
        ),
    ]
