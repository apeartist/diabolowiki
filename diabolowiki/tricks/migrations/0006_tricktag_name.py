# Generated by Django 5.1.6 on 2025-02-20 15:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tricks', '0005_alter_trick_tags_alter_tricktag_tricks'),
    ]

    operations = [
        migrations.AddField(
            model_name='tricktag',
            name='name',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
