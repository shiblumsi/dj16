# Generated by Django 3.1.2 on 2021-04-03 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_comment_replay_reply'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='t_view',
            field=models.IntegerField(default=0),
        ),
    ]
