# Generated by Django 4.0.5 on 2022-07-22 09:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('versioncheck', '0002_versioncheckv_delete_version_check'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='versioncheckv',
            name='state',
        ),
        migrations.AlterField(
            model_name='versioncheckv',
            name='importdate',
            field=models.DateTimeField(default=datetime.datetime(2022, 7, 22, 12, 3, 34, 455571)),
        ),
    ]