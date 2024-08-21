# Generated by Django 5.1 on 2024-08-13 05:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Profiles', '0007_alter_profile_prefix'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='Prefix',
            field=models.CharField(choices=[('Dr.', 'Dr.'), ('Mr.', 'Mr.'), ('Sir', 'Sir'), ('Lady', 'Lady'), ('Miss', 'Miss'), ('Dame', 'Dame'), ('Mx', 'Mx'), ('Mrs.', 'Mrs.'), ('Rev', 'Rev'), ('Ms.', 'Ms.'), ('Lord', 'Lord')], max_length=5),
        ),
    ]
