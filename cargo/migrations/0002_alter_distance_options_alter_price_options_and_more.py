# Generated by Django 4.1.1 on 2022-09-07 15:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cargo', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='distance',
            options={'ordering': ['id'], 'verbose_name': 'Расстояние', 'verbose_name_plural': 'Расстояние'},
        ),
        migrations.AlterModelOptions(
            name='price',
            options={'ordering': ['id'], 'verbose_name': 'Сумма', 'verbose_name_plural': 'Сумма'},
        ),
        migrations.AlterModelOptions(
            name='weight',
            options={'ordering': ['id'], 'verbose_name': 'Вес', 'verbose_name_plural': 'Вес'},
        ),
        migrations.AddField(
            model_name='distance',
            name='mone',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cargo.price'),
        ),
        migrations.AddField(
            model_name='price',
            name='kilo',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='cargo.weight'),
        ),
        migrations.AddField(
            model_name='price',
            name='km',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cargo.distance'),
        ),
    ]
