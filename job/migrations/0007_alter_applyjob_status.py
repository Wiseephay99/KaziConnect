# Generated by Django 5.0.6 on 2024-12-05 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('job', '0006_job_job_description_job_job_responsibilities_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applyjob',
            name='status',
            field=models.CharField(choices=[('Accepted', 'Accepted'), ('Pending', 'Pending'), ('Declined', 'Declined')], max_length=20),
        ),
    ]