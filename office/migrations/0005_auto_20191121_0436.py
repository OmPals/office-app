# Generated by Django 2.2.7 on 2019-11-21 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('office', '0004_auto_20191120_2118'),
    ]

    operations = [
        migrations.AlterField(
            model_name='visit',
            name='check_in',
            field=models.DateTimeField(),
        ),
        migrations.AlterField(
            model_name='visit',
            name='check_out',
            field=models.DateTimeField(),
        ),
    ]
