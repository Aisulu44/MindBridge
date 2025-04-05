# Generated by Django 5.1.6 on 2025-03-16 03:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_answer_discussion'),
    ]

    operations = [
        migrations.AddField(
            model_name='answer',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='replies', to='base.answer'),
        ),
    ]
