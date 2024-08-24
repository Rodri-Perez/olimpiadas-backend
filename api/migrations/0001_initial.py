# Generated by Django 5.1 on 2024-08-24 18:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cod', models.CharField(max_length=255)),
                ('categoria', models.CharField(max_length=255)),
                ('talle_peso', models.CharField(max_length=255)),
                ('nombre', models.CharField(max_length=255)),
                ('descripcion', models.CharField(max_length=255)),
                ('stock', models.PositiveIntegerField()),
                ('precio', models.PositiveIntegerField()),
            ],
        ),
    ]
