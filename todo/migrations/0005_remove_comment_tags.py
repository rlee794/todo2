# Generated by Django 4.0.4 on 2022-04-23 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0004_tag_comment_tags_task_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='tags',
        ),
    ]