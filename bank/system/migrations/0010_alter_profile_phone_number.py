# Generated by Django 5.0.1 on 2024-08-04 18:43

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("system", "0009_profile_phone_number_alter_transactions_amount"),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="phone_number",
            field=models.IntegerField(blank=True, default=0),
        ),
    ]
