# Generated by Django 2.1.5 on 2019-02-07 17:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0010_auto_20190207_1250'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment_page',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 2, 7, 12, 50, 13, 106352)),
        ),
    ]
