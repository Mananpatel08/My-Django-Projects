# Generated by Django 4.2.10 on 2025-03-22 09:34

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("ShoppyGo", "0005_customuser_date_of_birth_customuser_phone_number"),
    ]

    operations = [
        migrations.DeleteModel(
            name="UserProfile",
        ),
    ]
