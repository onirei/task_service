# Generated by Django 2.1.3 on 2019-04-13 17:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_list', '0006_auto_20190413_1742'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='create_date',
            field=models.DateField(default=datetime.date(2019, 4, 13)),
        ),
        migrations.AlterField(
            model_name='task',
            name='expiration_date',
            field=models.DateField(default=datetime.date(2019, 4, 13)),
        ),
    ]
