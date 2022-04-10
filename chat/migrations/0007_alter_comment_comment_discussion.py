# Generated by Django 4.0 on 2022-04-10 15:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0006_rename_custom_user_comment_comment_custom_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment_discussion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comment_discussion', to='chat.discussion'),
        ),
    ]