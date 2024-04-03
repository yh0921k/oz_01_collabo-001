# Generated by Django 5.0.3 on 2024-04-03 13:10

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("freelancer_users", "0001_initial"),
        ("terms", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="FreelancerTerm",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("agreed_at", models.DateTimeField(auto_now_add=True)),
                (
                    "term_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="terms.term"
                    ),
                ),
                (
                    "user_id",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="freelancer_users.freelanceruser",
                    ),
                ),
            ],
        ),
    ]
