# Generated by Django 2.1.3 on 2019-04-13 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_list', '0008_auto_20190413_2030'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='expiration_date',
            field=models.DateField(),
        ),
    ]