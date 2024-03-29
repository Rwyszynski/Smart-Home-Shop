# Generated by Django 5.0.2 on 2024-02-24 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=20)),
                ('model', models.CharField(max_length=32, unique=True)),
                ('voltage', models.PositiveSmallIntegerField(default=24)),
                ('power', models.PositiveSmallIntegerField(blank=True)),
                ('current', models.DecimalField(decimal_places=2, max_digits=6)),
                ('protocol', models.CharField(blank=True, max_length=10)),
                ('price', models.DecimalField(decimal_places=2, max_digits=6)),
            ],
        ),
    ]
