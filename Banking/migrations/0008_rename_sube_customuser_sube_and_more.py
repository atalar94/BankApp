# Generated by Django 4.0.4 on 2022-04-15 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Banking', '0007_alter_sube_kod'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='sube',
            new_name='Sube',
        ),
        migrations.RenameField(
            model_name='customuser',
            old_name='hesap_no',
            new_name='account_no',
        ),
        migrations.RenameField(
            model_name='customuser',
            old_name='bakiye',
            new_name='amount',
        ),
        migrations.AlterField(
            model_name='sube',
            name='kod',
            field=models.CharField(default=0, max_length=4, unique=True),
        ),
    ]