# Generated by Django 5.1.6 on 2025-03-16 03:14

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0005_remove_taggeditem_tag_remove_taggeditem_content_type_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='answer',
            name='discussion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answers', to='base.discussion'),
        ),
    ]
