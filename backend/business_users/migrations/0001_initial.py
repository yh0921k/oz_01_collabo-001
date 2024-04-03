# Generated by Django 5.0.3 on 2024-04-03 13:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("countries", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="BusinessUser",
            fields=[
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("id", models.AutoField(primary_key=True, serialize=False)),
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("company", models.CharField(max_length=50)),
                ("user_id", models.CharField(max_length=50, unique=True)),
                ("password", models.CharField(max_length=255)),
                ("mobile", models.IntegerField()),
                ("email", models.EmailField(max_length=255, unique=True)),
                ("language", models.CharField(max_length=50)),
                ("is_active", models.BooleanField(default=True)),
                (
                    "country",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        to="countries.country",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
