# Generated by Django 5.1.2 on 2024-11-02 12:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0002_medicalrecord'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Person',
        ),
    ]