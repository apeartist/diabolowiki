# Generated by Django 5.1.6 on 2025-02-11 14:59

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tricks', '0002_remove_trick_photo_trick_difficulty_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trick',
            name='instructions',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.TextField(blank=True, null=True), blank=True, default=list, size=None),
        ),
    ]
