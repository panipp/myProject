# Generated by Django 2.0.6 on 2018-07-27 09:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0020_auto_20180727_1547'),
    ]

    operations = [
        migrations.AlterField(
            model_name='question',
            name='type',
            field=models.CharField(choices=[('text', 'text (คำตอบยาว)'), ('short-text', 'short text (คำตอบสั้น)'), ('radio', 'choices')], default='text', max_length=200, verbose_name='Type'),
        ),
    ]
