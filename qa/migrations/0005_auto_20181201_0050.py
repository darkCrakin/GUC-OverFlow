# Generated by Django 2.1.3 on 2018-12-01 00:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qa', '0004_auto_20181130_2343'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='down_votes',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='question',
            name='down_votes',
            field=models.IntegerField(default=0),
        ),
    ]
