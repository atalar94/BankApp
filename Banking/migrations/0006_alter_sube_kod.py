# Generated by Django 4.0.4 on 2022-04-15 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Banking', '0005_alter_sube_kod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sube',
            name='kod',
            field=models.CharField(default='A Subesi', max_length=4, unique=True),
        ),
    ]
