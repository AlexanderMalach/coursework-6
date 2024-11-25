# Generated by Django 5.1.3 on 2024-11-19 20:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("newsletter", "0012_alter_mailing_date_time_last_mailing_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mailing",
            name="status",
            field=models.CharField(
                choices=[
                    ("CREATED", "Создана"),
                    ("STARTED", "Начата"),
                    ("FINISHED", "Завершена"),
                ],
                default="CREATED",
                max_length=10,
                verbose_name="Статус выполнения",
            ),
        ),
    ]
