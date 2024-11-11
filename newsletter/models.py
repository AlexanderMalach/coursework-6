from django.db import models
from django.utils import timezone

NULLABLE = {"blank": True, "null": True}


class Client(models.Model):
    email = models.EmailField(unique=True, verbose_name="email")
    fullname = models.CharField(max_length=250, verbose_name="ФИО")
    phone_number = models.CharField(max_length=15, unique=True, blank=True, **NULLABLE)
    comment = models.TextField(verbose_name="Комментарий")

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"

    def __str__(self):
        return f"{self.fullname}, {self.email}"


class Mailing(models.Model):
    class Frequency(models.TextChoices):
        DAILY = "daily", "День"
        WEEKLY = "weekly", "Неделя"
        MONTHLY = "monthly", "Месяц"

    class Status(models.TextChoices):
        CREATED = "created", "Создана"
        STARTED = "started", "Started"
        FINISHED = "finished", "Finished"

    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name="Клиент")
    datetime_first_mailing = models.DateTimeField(auto_now_add=True)
    frequency = models.CharField(max_length=10, choices=Frequency.choices)
    status = models.CharField(
        max_length=10, choices=Status.choices, default=Status.CREATED
    )

    class Meta:
        verbose_name = "Рассылка"
        verbose_name_plural = "Рассылки"

    def __str__(self):
        return f"{self.client}, {self.status}"


class Message(models.Model):
    subject = models.CharField(max_length=255, verbose_name="Тема")
    content = models.TextField(verbose_name="Содержание")

    class Meta:
        verbose_name = "Сообщение"
        verbose_name_plural = "Сообщения"

    def __str__(self):
        return self.subject


class MailingAttempt(models.Model):
    class Status(models.TextChoices):
        SUCCESS = "success", "Успешно"
        FAILED = "failed", "Неуспешно"

    mailing = models.ForeignKey(
        Mailing, on_delete=models.SET_NULL, verbose_name="Рассылка"
    )
    datetime_attempt = models.DateTimeField(
        default=timezone.now,
        verbose_name="Дата и время попытки рассылки",
    )
    status = models.CharField(
        max_length=10, choices=Status.choices, default=Status.SUCCESS, **NULLABLE
    )
    server_response = models.TextField(**NULLABLE, verbose_name="Отклик сервера")