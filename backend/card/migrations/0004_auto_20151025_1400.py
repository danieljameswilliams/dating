# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0003_auto_20151025_1359'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='association',
            field=models.ForeignKey(related_name='Card_association', blank=True, to='card.Association', null=True),
        ),
    ]
