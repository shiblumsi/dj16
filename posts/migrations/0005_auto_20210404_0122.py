# Generated by Django 3.1.2 on 2021-04-03 19:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_post_t_view'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment_replay',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='comment_replay',
            name='reply',
        ),
        migrations.RemoveField(
            model_name='post',
            name='t_view',
        ),
    ]
