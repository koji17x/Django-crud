# Generated by Django 5.1 on 2024-09-30 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taks', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='category',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AddField(
            model_name='task',
            name='due_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='datacompleted',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
