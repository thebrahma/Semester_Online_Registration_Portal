# Generated by Django 2.0.5 on 2018-07-15 18:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sorp_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentinfo',
            name='institute',
            field=models.CharField(default='NIT Hamirpur', max_length=16),
            preserve_default=False,
        ),
    ]