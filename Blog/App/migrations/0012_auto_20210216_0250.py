# Generated by Django 3.1.6 on 2021-02-16 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0011_auto_20210216_0249'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='status',
            field=models.CharField(choices=[('PUBLISHED', 'PUBLISHED'), ('PANNED', 'PANNED')], default='PUBLISHED', max_length=50, null=True),
        ),
    ]
