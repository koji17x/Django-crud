# Generated by Django 5.1 on 2024-10-03 04:47

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taks', '0004_delete_advance'),
    ]

    operations = [
        migrations.CreateModel(
            name='Avances',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('avance_description', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='avances', to='taks.task')),
            ],
        ),
    ]
