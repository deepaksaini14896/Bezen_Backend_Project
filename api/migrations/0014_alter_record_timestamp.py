# Generated by Django 4.0.3 on 2022-03-28 18:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_alter_record_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='timestamp',
            field=models.DateField(blank=True, default=datetime.datetime(2022, 3, 28, 18, 31, 18, 341774)),
        ),
    ]