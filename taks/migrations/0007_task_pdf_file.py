# Generated by Django 5.1 on 2024-10-04 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taks', '0006_advance_delete_avances'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='pdf_file',
            field=models.FileField(blank=True, null=True, upload_to='pdfs/'),
        ),
    ]
