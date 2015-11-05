# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('zip', models.CharField(max_length=15, null=True)),
                ('city', models.CharField(max_length=50, null=True)),
                ('country', models.CharField(max_length=50, null=True)),
                ('latitude', models.CharField(max_length=50, null=True)),
                ('longitude', models.CharField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('name', models.CharField(max_length=200)),
                ('location', models.ForeignKey(related_name='Profile_location', to='profile.Location')),
                ('user', models.ForeignKey(related_name='Profile_user', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
