# Generated by Django 5.0.4 on 2024-04-30 17:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('centre', '0002_assignatura'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuari',
            name='assignatures',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='centre.assignatura'),
        ),
    ]
