# Generated by Django 5.0.3 on 2024-03-27 16:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_docsection_positionaltag_docsection'),
    ]

    operations = [
        migrations.AlterField(
            model_name='positionaltag',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='app.project'),
        ),
    ]
