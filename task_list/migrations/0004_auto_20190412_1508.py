# Generated by Django 2.1.3 on 2019-04-12 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_list', '0003_auto_20190411_2054'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='about',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='task',
            name='expiration_date',
            field=models.DateField(),
        ),
    ]