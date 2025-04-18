# Generated by Django 5.1.7 on 2025-04-14 22:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0008_alter_delivery_header_delivery_number"),
    ]

    operations = [
        migrations.AlterField(
            model_name="customers",
            name="customer_code",
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name="delivery_header",
            name="delivery_number",
            field=models.CharField(max_length=20, unique=True),
        ),
    ]
