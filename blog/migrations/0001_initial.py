# Generated by Django 5.0.7 on 2024-11-28 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Blog",
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
                (
                    "title",
                    models.CharField(
                        help_text="Напишите заголовок",
                        max_length=100,
                        verbose_name="Заголовок",
                    ),
                ),
                (
                    "text",
                    models.TextField(
                        blank=True,
                        help_text="Напишите текст статьи",
                        null=True,
                        verbose_name="Текст статьи",
                    ),
                ),
                (
                    "image",
                    models.ImageField(
                        blank=True,
                        help_text="Загрузите изображение",
                        null=True,
                        upload_to="blogs/",
                        verbose_name="Изображение",
                    ),
                ),
                (
                    "views_count",
                    models.PositiveIntegerField(
                        default=0,
                        help_text="Укажите количество просмотров",
                        verbose_name="Количество просмотров",
                    ),
                ),
                ("date", models.DateField(auto_now_add=True)),
                ("date_update", models.DateField(auto_now=True)),
            ],
            options={
                "verbose_name": "Блог",
                "verbose_name_plural": "Блог",
                "permissions": [
                    ("can_add_blog", "Can add blog"),
                    ("can_view_blog", "Can view blog"),
                    ("can_change_blog", "Can change blog"),
                    ("can_delete_blog", "Can delete blog"),
                ],
            },
        ),
    ]
