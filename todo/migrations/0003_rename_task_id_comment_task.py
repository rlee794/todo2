# Generated by Django 4.0.4 on 2022-04-22 19:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_alter_task_id_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='task_id',
            new_name='task',
        ),
    ]