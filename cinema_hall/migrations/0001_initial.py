# Generated by Django 5.1.6 on 2025-02-22 08:28

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hall',
            fields=[
                ('hall_id', models.AutoField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('hall_name', models.CharField(max_length=250)),
                ('hall_address', models.CharField(max_length=250)),
                ('hall_city', models.CharField(max_length=250)),
            ],
        ),
    ]
