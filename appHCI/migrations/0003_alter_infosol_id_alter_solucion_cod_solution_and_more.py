# Generated by Django 4.2.3 on 2023-08-27 06:24

from django.db import migrations, models
import shortuuid.main
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('appHCI', '0002_alter_infosol_id_alter_solucion_cod_solution_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infosol',
            name='id',
            field=models.CharField(default=uuid.UUID('a541e390-aa9d-465f-9c1c-0230ca65158a'), editable=False, max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='solucion',
            name='cod_solution',
            field=models.CharField(default=shortuuid.main.ShortUUID.uuid, max_length=7, unique=True),
        ),
        migrations.AlterField(
            model_name='solucion',
            name='id',
            field=models.CharField(default=uuid.UUID('024545f3-e6c5-46d5-b5d9-3677af6d5e28'), editable=False, max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='suscritos',
            name='id',
            field=models.CharField(default=uuid.UUID('fdd518b7-c17b-444d-9596-047c8c576f14'), editable=False, max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='trabaja',
            name='id',
            field=models.CharField(default=uuid.UUID('919d9283-6836-4d78-8bc8-9a7c141227d8'), editable=False, max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='typeuser',
            name='id',
            field=models.CharField(default=uuid.UUID('6922154f-cb62-4dd3-9345-bf547b172f0e'), editable=False, max_length=36, primary_key=True, serialize=False),
        ),
    ]
