# Generated by Django 4.0.4 on 2022-04-15 15:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Banking', '0002_alter_sube_kod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sube',
            name='kod',
            field=models.CharField(default='ASUBESİ', max_length=4, unique=True),
        ),
    ]
