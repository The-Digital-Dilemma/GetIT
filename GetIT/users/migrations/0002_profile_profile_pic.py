# Generated by Django 4.2.2 on 2023-06-30 00:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="profile",
            name="profile_pic",
            field=models.ImageField(blank=True, upload_to="profile_pics/"),
        ),
    ]