# Generated by Django 4.2.6 on 2023-10-27 15:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_contact_site_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='ceremony',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
