# Generated by Django 2.1.3 on 2019-04-10 13:46

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('about', models.TextField(max_length=2000)),
                ('image', models.ImageField(upload_to='img')),
                ('create_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('expiration_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('status', models.CharField(max_length=64)),
            ],
        ),
    ]