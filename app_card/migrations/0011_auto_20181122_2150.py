# Generated by Django 2.0.7 on 2018-11-22 19:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_card', '0010_auto_20180925_1232'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medexamination',
            name='dat_end',
            field=models.DateField(default=datetime.datetime(2020, 11, 22, 21, 50, 49, 94969), verbose_name='Дата действия справки'),
        ),
        migrations.AlterField(
            model_name='medexamination',
            name='patient_status',
            field=models.CharField(blank=True, choices=[('Да', 'Да'), ('Нет', 'Нет')], default='Нет', help_text='Введите статус уведомления', max_length=3, verbose_name='Статус'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='date_update',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
