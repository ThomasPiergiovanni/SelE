# Generated by Django 4.0 on 2022-03-25 05:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0007_alter_customuser_collectivity'),
        ('vote', '0003_remove_voting_custom_user_voting_voting_custom_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vote',
            name='custom_user',
        ),
        migrations.RemoveField(
            model_name='vote',
            name='voting',
        ),
        migrations.AddField(
            model_name='vote',
            name='vote_custom_user',
            field=models.ForeignKey(default=7, on_delete=django.db.models.deletion.CASCADE, related_name='vote_custom_user', to='authentication.customuser'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='vote',
            name='vote_voting',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='vote_voting', to='vote.voting'),
            preserve_default=False,
        ),
    ]
