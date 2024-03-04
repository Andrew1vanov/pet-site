# Generated by Django 5.0.2 on 2024-02-25 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Security',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('short_name', models.CharField(max_length=100)),
                ('sec_id', models.CharField(max_length=10)),
                ('board', models.CharField(max_length=4)),
                ('slug', models.SlugField(max_length=120)),
            ],
            options={
                'verbose_name': 'security',
                'verbose_name_plural': 'securities',
                'ordering': ['name'],
                'indexes': [models.Index(fields=['name'], name='shares_secu_name_be4d3f_idx'), models.Index(fields=['id', 'slug'], name='shares_secu_id_c73e81_idx')],
            },
        ),
    ]