# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipn', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paypalipn',
            name='eu_id',
            field=models.IntegerField(null=True),
        ),
    ]
