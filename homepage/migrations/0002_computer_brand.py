# Generated by Django 5.1.5 on 2025-01-19 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='computer',
            name='brand',
            field=models.CharField(default='Unkown', max_length=200),
            preserve_default=False,
        ),
    ]
