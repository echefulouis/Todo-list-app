# Generated by Django 3.0.6 on 2020-05-28 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Done',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('done_date', models.DateTimeField(verbose_name='Date Added')),
                ('done_text', models.CharField(max_length=200)),
            ],
        ),
    ]
