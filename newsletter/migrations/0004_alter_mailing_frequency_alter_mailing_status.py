# Generated by Django 5.1.3 on 2024-11-14 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("newsletter", "0003_mailing_interval"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mailing",
            name="frequency",
            field=models.CharField(
                choices=[("day", "День"), ("week", "Неделя"), ("month", "Месяц")],
                max_length=10,
                verbose_name="Периодичность рассылки",
            ),
        ),
        migrations.AlterField(
            model_name="mailing",
            name="status",
            field=models.CharField(
                choices=[
                    ("created", "Создана"),
                    ("started", "Начата"),
                    ("finished", "Завершена"),
                ],
                default="created",
                max_length=10,
                verbose_name="Статус выполнения",
            ),
        ),
    ]