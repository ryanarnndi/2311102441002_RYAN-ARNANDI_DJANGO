# Generated by Django 5.1.7 on 2025-05-01 01:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pengguna', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='biodata',
            name='foto',
            field=models.ImageField(blank=True, null=True, upload_to='pengguna'),
        ),
    ]
