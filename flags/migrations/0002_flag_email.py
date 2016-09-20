# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('flags', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flag',
            name='email',
            field=models.CharField(default='example@example.com', max_length=50),
            preserve_default=False,
        ),
    ]
