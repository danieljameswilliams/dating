# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0001_initial'),
        ('profile', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('is_active', models.BooleanField(default=False)),
                ('card', models.ForeignKey(related_name='Match_card', to='card.Card')),
            ],
        ),
        migrations.CreateModel(
            name='MatchItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('card_profile1', models.ForeignKey(related_name='MatchItem_card_profile1', to='card.Card')),
                ('card_profile2', models.ForeignKey(related_name='MatchItem_card_profile2', to='card.Card')),
            ],
        ),
        migrations.AddField(
            model_name='match',
            name='matches',
            field=models.ManyToManyField(related_name='Match_matches', to='match.MatchItem'),
        ),
        migrations.AddField(
            model_name='match',
            name='profile1',
            field=models.ForeignKey(related_name='Match_profile1', to='profile.Profile'),
        ),
        migrations.AddField(
            model_name='match',
            name='profile2',
            field=models.ForeignKey(related_name='Match_profile2', to='profile.Profile'),
        ),
    ]
