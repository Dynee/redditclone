# Generated by Django 3.1.6 on 2021-02-07 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('subreddit', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='post_id',
            new_name='post',
        ),
        migrations.RenameField(
            model_name='comment',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='subreddit_id',
            new_name='subreddit',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='user_id',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='subreddit',
            old_name='user_id',
            new_name='user',
        ),
    ]
