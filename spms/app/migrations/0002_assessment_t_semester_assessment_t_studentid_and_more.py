# Generated by Django 4.1.7 on 2023-04-19 16:50

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='assessment_t',
            name='semester',
            field=models.CharField(blank=True, choices=[('Spring', 'Spring'), ('Summer', 'Summer'), ('Autumn', 'Autumn')], max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='assessment_t',
            name='studentID',
            field=models.ForeignKey(default=1830398, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='assessment_t',
            name='year',
            field=models.CharField(default=2022, max_length=4),
            preserve_default=False,
        ),
    ]
