# Generated by Django 5.1 on 2024-08-11 05:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profiles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='Prefix',
            field=models.CharField(blank=True, max_length=5),
        ),
    ]
