# Generated by Django 3.1.6 on 2021-02-07 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('subreddit', '0002_auto_20210207_2025'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subreddit',
            name='name',
            field=models.CharField(max_length=25, unique=True),
        ),
    ]
