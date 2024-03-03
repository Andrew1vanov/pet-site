# Generated by Django 5.0.2 on 2024-03-03 16:12

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shares', '0002_security_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='security',
            name='price',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.FloatField(), default=None, size=None),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='security',
            name='volume',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.IntegerField(), default=None, size=None),
            preserve_default=False,
        ),
    ]
