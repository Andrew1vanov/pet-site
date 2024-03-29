# Generated by Django 5.0.2 on 2024-03-08 14:45

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shares', '0004_alter_security_volume'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='security',
            options={'ordering': ['short_name'], 'verbose_name': 'security', 'verbose_name_plural': 'securities'},
        ),
        migrations.AddField(
            model_name='security',
            name='users_like',
            field=models.ManyToManyField(blank=True, related_name='securities_liked', to=settings.AUTH_USER_MODEL),
        ),
    ]
