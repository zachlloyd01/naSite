# Generated by Django 2.1.5 on 2019-02-06 01:04

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0004_comment_page'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment_page',
            name='date',
            field=models.DateField(default=datetime.datetime(2019, 2, 5, 20, 4, 21, 205745)),
        ),
    ]
