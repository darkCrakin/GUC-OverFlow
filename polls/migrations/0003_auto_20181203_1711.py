# Generated by Django 2.1.3 on 2018-12-03 17:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_auto_20181203_1658'),
    ]

    operations = [
        migrations.RenameField(
            model_name='poll',
            old_name='User',
            new_name='gucian',
        ),
    ]
