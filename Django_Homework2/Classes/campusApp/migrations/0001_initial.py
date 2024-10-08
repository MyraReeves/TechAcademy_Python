# Generated by Django 5.1 on 2024-08-22 03:34

import django.db.models.manager
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UniversityCampus',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Campus_Name', models.CharField(blank=True, default='', max_length=50)),
                ('City', models.CharField(blank=True, default='', max_length=60)),
                ('State', models.CharField(blank=True, default='', max_length=2)),
                ('Campus_ID', models.IntegerField(blank=True, default='')),
            ],
            options={
                'verbose_name_plural': 'University Campus',
            },
            managers=[
                ('object', django.db.models.manager.Manager()),
            ],
        ),
    ]
