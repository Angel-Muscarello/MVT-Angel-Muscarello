# Generated by Django 3.2.15 on 2022-10-01 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppCoder', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='familiar',
            name='fecha_de_nacimiento',
            field=models.DateField(auto_now=True),
        ),
    ]
