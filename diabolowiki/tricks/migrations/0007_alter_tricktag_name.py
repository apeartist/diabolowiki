# Generated by Django 5.1.6 on 2025-02-21 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tricks', '0006_tricktag_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tricktag',
            name='name',
            field=models.CharField(max_length=30),
        ),
    ]
