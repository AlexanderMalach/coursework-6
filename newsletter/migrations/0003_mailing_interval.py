# Generated by Django 5.1.3 on 2024-11-13 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("newsletter", "0002_alter_mailingattempt_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="mailing",
            name="interval",
            field=models.PositiveIntegerField(
                default=60, verbose_name="Интервал между рассылками (минуты)"
            ),
        ),
    ]
