# Generated by Django 5.1 on 2024-09-03 19:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('alterego', models.CharField(max_length=100, verbose_name='Альтер эго')),
                ('debut', models.IntegerField(verbose_name='Год появления')),
                ('gender', models.CharField(max_length=100, verbose_name='Пол')),
                ('occupation', models.CharField(max_length=100, verbose_name='Позиция')),
                ('description', models.TextField(verbose_name='Описание')),
                ('skills', models.TextField(verbose_name='Способности')),
                ('background', models.TextField(verbose_name='Предыстория')),
                ('appearance', models.TextField(verbose_name='Внешность')),
                ('alliess', models.TextField(verbose_name='Союзники')),
                ('enemises', models.TextField(verbose_name='Враги')),
            ],
        ),
    ]
