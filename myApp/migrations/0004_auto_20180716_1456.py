# Generated by Django 2.0.6 on 2018-07-16 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0003_question'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='order',
        ),
        migrations.AddField(
            model_name='question',
            name='choices',
            field=models.TextField(blank=True, null=True, verbose_name='Choices'),
        ),
    ]
