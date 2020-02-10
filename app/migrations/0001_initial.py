# Generated by Django 3.0.3 on 2020-02-10 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contactRequest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=2, verbose_name='')),
                ('email', models.EmailField(max_length=254)),
                ('plan', models.IntegerField(choices=[(100, '100SAR'), (200, '200SAR'), (300, '300SAR')], default=2, verbose_name='Plan')),
            ],
        ),
    ]