# Generated by Django 4.1.3 on 2022-12-14 07:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_jadwalsholat_alter_artikel_options'),
    ]

    operations = [
        migrations.RenameField(
            model_name='jadwalsholat',
            old_name='ashar',
            new_name='jadwals',
        ),
        migrations.RenameField(
            model_name='jadwalsholat',
            old_name='dhuha',
            new_name='waktu',
        ),
    ]
