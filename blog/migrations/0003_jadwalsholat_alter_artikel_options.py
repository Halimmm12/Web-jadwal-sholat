# Generated by Django 4.1.3 on 2022-12-08 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_alter_artikel_options_alter_kategori_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='JadwalSholat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imam', models.CharField(blank=True, max_length=30, null=True)),
                ('ashar', models.CharField(blank=True, max_length=30, null=True)),
                ('dhuha', models.CharField(blank=True, max_length=30, null=True)),
                ('tanggal', models.DateField(blank=True, null=True)),
            ],
        ),
        migrations.AlterModelOptions(
            name='artikel',
            options={'ordering': ['-date'], 'verbose_name_plural': 'Artikel'},
        ),
    ]