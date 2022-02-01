# Generated by Django 4.0 on 2022-02-01 21:32

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0005_alter_customuser_email_alter_customuser_user_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('proposition', '0011_proposition_relation_custom_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='proposition',
            name='relation_custom_user',
        ),
        migrations.AddField(
            model_name='proposition',
            name='blocked_takers',
            field=models.ManyToManyField(related_name='blocked_takers', through='proposition.BlockedTaker', to=settings.AUTH_USER_MODEL),
        ),
    ]
