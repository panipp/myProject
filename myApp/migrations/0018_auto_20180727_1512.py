# Generated by Django 2.0.6 on 2018-07-27 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myApp', '0017_remove_survey_template'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=400, verbose_name='Name')),
                ('description', models.CharField(blank=True, max_length=2000, null=True, verbose_name='Description')),
                ('survey', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='categories', to='myApp.Survey', verbose_name='Survey')),
            ],
            options={
                'verbose_name': 'category',
                'verbose_name_plural': 'categories',
            },
        ),
        migrations.AlterModelOptions(
            name='question',
            options={},
        ),
        migrations.AddField(
            model_name='question',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='questions', to='myApp.Category', verbose_name='Category'),
        ),
    ]
