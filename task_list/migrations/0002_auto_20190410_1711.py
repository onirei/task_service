# Generated by Django 2.1.3 on 2019-04-10 14:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('task_list', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='create_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='task',
            name='expiration_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
