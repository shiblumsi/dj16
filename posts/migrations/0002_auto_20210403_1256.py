# Generated by Django 3.1.2 on 2021-04-03 06:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment_replay',
            name='d',
        ),
        migrations.RemoveField(
            model_name='person',
            name='d',
        ),
        migrations.RemoveField(
            model_name='post',
            name='d',
        ),
    ]
