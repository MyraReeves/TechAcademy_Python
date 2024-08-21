# Generated by Django 5.1 on 2024-08-13 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profiles', '0005_alter_profile_prefix'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Prefix',
            field=models.CharField(choices=[('Mrs.', 'Mrs.'), ('Lady', 'Lady'), ('Mx', 'Mx'), ('Lord', 'Lord'), ('Dr.', 'Dr.'), ('Miss', 'Miss'), ('Sir', 'Sir'), ('Mr.', 'Mr.'), ('Rev', 'Rev'), ('Dame', 'Dame'), ('Ms.', 'Ms.')], max_length=5),
        ),
    ]
