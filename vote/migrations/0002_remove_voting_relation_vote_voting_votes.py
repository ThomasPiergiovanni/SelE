# Generated by Django 4.0 on 2022-03-12 17:27

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0007_alter_customuser_collectivity'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('vote', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='voting',
            name='relation_vote',
        ),
        migrations.AddField(
            model_name='voting',
            name='votes',
            field=models.ManyToManyField(related_name='votes', through='vote.Vote', to=settings.AUTH_USER_MODEL),
        ),
    ]