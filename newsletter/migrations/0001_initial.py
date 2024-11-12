# Generated by Django 5.0.7 on 2024-11-12 09:14

import django.db.models.deletion
import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email')),
                ('fullname', models.CharField(max_length=250, verbose_name='ФИО')),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True, unique=True)),
                ('comment', models.TextField(verbose_name='Комментарий')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255, verbose_name='Тема')),
                ('content', models.TextField(verbose_name='Содержание')),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
            },
        ),
        migrations.CreateModel(
            name='Mailing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_first_mailing', models.DateTimeField(auto_now_add=True)),
                ('frequency', models.CharField(choices=[('daily', 'День'), ('weekly', 'Неделя'), ('monthly', 'Месяц')], max_length=10)),
                ('status', models.CharField(choices=[('created', 'Создана'), ('started', 'Начата'), ('finished', 'Завершена')], default='created', max_length=10)),
                ('clients', models.ManyToManyField(to='newsletter.client', verbose_name='Клиенты')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='newsletter.message', verbose_name='Сообщение')),
            ],
            options={
                'verbose_name': 'Рассылка',
                'verbose_name_plural': 'Рассылки',
            },
        ),
        migrations.CreateModel(
            name='MailingAttempt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime_attempt', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата и время попытки рассылки')),
                ('status', models.CharField(blank=True, choices=[('success', 'Успешно'), ('failed', 'Неуспешно')], default='success', max_length=10, null=True)),
                ('server_response', models.TextField(blank=True, null=True, verbose_name='Отклик сервера')),
                ('mailing', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='attempts', to='newsletter.mailing', verbose_name='Рассылка')),
            ],
        ),
    ]