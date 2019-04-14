# Generated by Django 2.1.3 on 2019-04-11 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task_list', '0002_auto_20190410_1711'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('Open', 'Open'), ('Needs offer', 'Needs offer'), ('Offered', 'Offered'), ('Approved', 'Approved'), ('In progress', 'In progress'), ('Ready', 'Ready'), ('Verified', 'Verified'), ('Closed', 'Closed')], default='Open', max_length=64),
        ),
    ]