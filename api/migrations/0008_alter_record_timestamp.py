# Generated by Django 4.0.3 on 2022-03-28 18:30

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_alter_record_timestamp'),
    ]

    operations = [
        migrations.AlterField(
            model_name='record',
            name='timestamp',
            field=models.DateField(default=datetime.datetime(2022, 3, 28, 18, 30, 39, 569808), null=True),
        ),
    ]
