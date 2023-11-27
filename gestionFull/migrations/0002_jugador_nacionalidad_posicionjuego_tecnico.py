# Generated by Django 4.2.7 on 2023-11-26 17:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gestionFull', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('foto', models.ImageField(upload_to='imagenes/')),
                ('fecha_nacimiento', models.DateField()),
                ('posicion', models.CharField(max_length=50)),
                ('numero_camiseta', models.PositiveIntegerField()),
                ('titular', models.BooleanField(default=False)),
                ('equipo', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Nacionalidad',
            fields=[
                ('codigo', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name_plural': 'Nacionalidades',
                'db_table': 'nacionalidad',
            },
        ),
        migrations.CreateModel(
            name='PosicionJuego',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Tecnico',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('fecha_nacimiento', models.DateField()),
                ('rol', models.CharField(choices=[('TEC', 'Técnico'), ('ASI', 'Asistente'), ('MED', 'Médico'), ('PRE', 'Preparador')], max_length=3)),
                ('nacionalidad', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionFull.nacionalidad')),
            ],
            options={
                'verbose_name_plural': 'Técnicos',
                'db_table': 'tecnico',
            },
        ),
    ]