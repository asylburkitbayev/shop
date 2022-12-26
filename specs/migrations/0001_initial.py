# Generated by Django 4.1.4 on 2022-12-26 06:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryFeature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feature_name', models.CharField(max_length=99, verbose_name='Имя ключа категории')),
                ('feature_filter_name', models.CharField(max_length=99, verbose_name='Имя для фильтрации')),
                ('unit', models.CharField(blank=True, max_length=44, null=True, verbose_name='Единица измерения')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.category', verbose_name='Категория')),
            ],
        ),
        migrations.CreateModel(
            name='ProductFeature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=255, verbose_name='Значение')),
                ('feature', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='specs.categoryfeature', verbose_name='Характеристика')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.product', verbose_name='Товар')),
            ],
        ),
        migrations.CreateModel(
            name='FeatureValidator',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valid_feature_value', models.CharField(max_length=123, verbose_name='Валидное значение')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.category', verbose_name='Категория')),
                ('feature_key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='specs.categoryfeature', verbose_name='Ключ характеристики')),
            ],
        ),
    ]
