# Generated by Django 2.0.5 on 2018-06-26 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sorp_app', '0004_auto_20180625_0645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subjects',
            name='id',
            field=models.SmallIntegerField(default=1, primary_key=True),
            preserve_default=False,
        ),
    ]
