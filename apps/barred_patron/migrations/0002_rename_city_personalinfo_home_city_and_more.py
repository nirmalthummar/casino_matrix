# Generated by Django 4.1.4 on 2022-12-11 18:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('barred_patron', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='personalinfo',
            old_name='city',
            new_name='home_city',
        ),
        migrations.RenameField(
            model_name='personalinfo',
            old_name='state',
            new_name='home_state',
        ),
        migrations.RenameField(
            model_name='personalinfo',
            old_name='street',
            new_name='home_street',
        ),
        migrations.RenameField(
            model_name='personalinfo',
            old_name='zipcode',
            new_name='home_zipcode',
        ),
    ]