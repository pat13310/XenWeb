# Generated by Django 5.1.3 on 2024-11-16 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_rename_date_of_birth_userprofile_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='birthday',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
