# Generated by Django 5.0.4 on 2024-04-30 16:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rol',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Usuari',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=255)),
                ('cognom', models.CharField(max_length=255)),
                ('assignatures', models.CharField(max_length=255)),
                ('rol', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='centre.rol')),
            ],
        ),
    ]
