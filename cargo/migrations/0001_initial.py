# Generated by Django 4.1.1 on 2022-09-07 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Distance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Координаты')),
                ('longitude_1', models.IntegerField(verbose_name='Долгота_1')),
                ('longitude_2', models.IntegerField(verbose_name='Долгота_2')),
                ('latitude_1', models.IntegerField(verbose_name='Широта_1')),
                ('latitude_2', models.IntegerField(verbose_name='Широта_2')),
            ],
        ),
        migrations.CreateModel(
            name='Price',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Сумма')),
                ('money', models.IntegerField(verbose_name='Широта')),
            ],
        ),
        migrations.CreateModel(
            name='Weight',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Вес')),
                ('kilo', models.IntegerField(verbose_name='Широта')),
            ],
        ),
    ]
