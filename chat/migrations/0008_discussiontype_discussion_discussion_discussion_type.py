# Generated by Django 4.0 on 2022-04-14 14:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0007_alter_comment_comment_discussion'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiscussionType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default=None, max_length=32, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='discussion',
            name='discussion_discussion_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='discussion_discussion_type', to='chat.discussiontype'),
        ),
    ]
