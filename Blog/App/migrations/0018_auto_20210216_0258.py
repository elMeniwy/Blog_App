# Generated by Django 3.1.6 on 2021-02-16 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0017_post_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(null=True, upload_to='images'),
        ),
    ]
