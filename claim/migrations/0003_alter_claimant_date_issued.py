# Generated by Django 4.2.12 on 2025-04-19 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("claim", "0002_claimant_user"),
    ]

    operations = [
        migrations.AlterField(
            model_name="claimant",
            name="date_issued",
            field=models.DateField(auto_now_add=True),
        ),
    ]
