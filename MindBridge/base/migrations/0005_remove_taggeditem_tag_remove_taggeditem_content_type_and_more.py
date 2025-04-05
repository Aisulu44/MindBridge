# Generated by Django 5.1.6 on 2025-03-16 01:24

import taggit.managers
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_customtag_alter_discussion_options_taggeditem_and_more'),
        ('taggit', '0006_rename_taggeditem_content_type_object_id_taggit_tagg_content_8fc721_idx'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taggeditem',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='taggeditem',
            name='content_type',
        ),
        migrations.AddField(
            model_name='discussion',
            name='participants',
            field=models.ManyToManyField(blank=True, related_name='participants', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='discussion',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.DeleteModel(
            name='CustomTag',
        ),
        migrations.DeleteModel(
            name='TaggedItem',
        ),
    ]
