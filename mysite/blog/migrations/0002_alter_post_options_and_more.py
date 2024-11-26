# Generated by Django 5.1.2 on 2024-11-26 12:58

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='post',
            options={'ordering': ('-publish',)},
        ),
        migrations.RemoveIndex(
            model_name='post',
            name='blog_post_publish_493ec4_idx',
        ),
        migrations.RenameField(
            model_name='post',
            old_name='published',
            new_name='publish',
        ),
        migrations.AddIndex(
            model_name='post',
            index=models.Index(fields=['-publish'], name='blog_post_publish_bb7600_idx'),
        ),
    ]
