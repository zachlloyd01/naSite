# Generated by Django 2.1.5 on 2019-02-06 17:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0005_comment_page_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment_page',
            name='date',
        ),
    ]
