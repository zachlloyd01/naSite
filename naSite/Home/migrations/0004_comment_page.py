# Generated by Django 2.1.5 on 2019-02-06 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_auto_20190204_2221'),
    ]

    operations = [
        migrations.CreateModel(
            name='comment_page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=400)),
                ('comment', models.TextField(default='', max_length=1000)),
            ],
        ),
    ]
