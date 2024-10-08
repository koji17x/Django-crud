# Generated by Django 5.1 on 2024-10-03 14:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taks', '0005_avances'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('progress_description', models.TextField()),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='advances', to='taks.task')),
            ],
        ),
        migrations.DeleteModel(
            name='Avances',
        ),
    ]
