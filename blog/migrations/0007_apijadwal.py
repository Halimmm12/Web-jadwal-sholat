# Generated by Django 4.1.3 on 2022-12-17 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_jadwalsholat_tanggal'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApiJadwal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tanggal', models.DateField(max_length=255, unique=True)),
                ('imsyak', models.TimeField()),
                ('shubuh', models.TimeField()),
                ('terbit', models.TimeField()),
                ('dhuha', models.TimeField()),
                ('dzuhur', models.TimeField()),
                ('ashr', models.TimeField()),
                ('magrib', models.TimeField()),
                ('isya', models.TimeField()),
            ],
        ),
    ]
