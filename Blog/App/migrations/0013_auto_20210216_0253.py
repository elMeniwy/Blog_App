# Generated by Django 3.1.6 on 2021-02-16 00:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0012_auto_20210216_0250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(max_length=1600, null=True),
        ),
    ]
