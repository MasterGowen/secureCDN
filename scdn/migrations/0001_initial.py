# Generated by Django 4.1.3 on 2022-11-11 21:17

from django.db import migrations, models
import django.db.models.deletion
import versionfield.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True, default='')),
            ],
        ),
        migrations.CreateModel(
            name='Resource',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', versionfield.fields.VersionField()),
                ('title', models.CharField(max_length=30)),
                ('file', models.FileField(upload_to='upload/files/')),
                ('library', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scdn.library')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='scdn.resource')),
            ],
        ),
        migrations.CreateModel(
            name='Permissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allow_all', models.BooleanField(default=False)),
                ('regex', models.CharField(max_length=64)),
                ('library', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scdn.library')),
                ('resource', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scdn.resource')),
            ],
        ),
    ]