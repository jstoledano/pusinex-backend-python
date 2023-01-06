# Generated by Django 4.1.5 on 2023-01-05 15:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('control', '0004_alter_localidad_cabecera'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pusinex',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_actual', models.DateField()),
                ('hojas', models.PositiveSmallIntegerField()),
                ('observaciones', models.TextField()),
                ('archivo', models.FileField(upload_to='media')),
                ('localidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='control.localidad')),
                ('seccion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='control.seccion')),
            ],
            options={
                'verbose_name': 'PUSINEX',
                'verbose_name_plural': 'PUSINEXs',
            },
        ),
    ]
