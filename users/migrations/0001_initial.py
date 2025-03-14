# Generated by Django 5.1.6 on 2025-02-23 07:06

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=250)),
                ('phone_number', models.CharField(max_length=10)),
                ('city_preference', models.JSONField(default=list)),
            ],
        ),
    ]
