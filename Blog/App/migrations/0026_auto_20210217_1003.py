# Generated by Django 3.1.6 on 2021-02-17 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0025_auto_20210217_0838'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='status',
        ),
        migrations.AddField(
            model_name='post',
            name='publish',
            field=models.BooleanField(default=True),
        ),
    ]