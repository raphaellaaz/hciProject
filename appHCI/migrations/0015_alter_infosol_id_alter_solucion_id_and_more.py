# Generated by Django 4.2.3 on 2023-08-16 14:29

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('appHCI', '0014_alter_infosol_id_alter_solucion_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infosol',
            name='id',
            field=models.UUIDField(default=uuid.UUID('c091adcb-7ebf-43bd-ad87-315268c87495'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='solucion',
            name='id',
            field=models.UUIDField(default=uuid.UUID('9158d05e-5c77-4551-b4a7-e673b5accc19'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='suscritos',
            name='id',
            field=models.UUIDField(default=uuid.UUID('4f294df4-5b0c-4a16-b69d-9a396ac524f8'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='trabaja',
            name='id',
            field=models.UUIDField(default=uuid.UUID('16deb96f-0089-4131-86b5-5840d3eca135'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='typeuser',
            name='id',
            field=models.IntegerField(default=uuid.UUID('0fa596a5-9fb6-440c-8a56-00724f3c6b50'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='u_negocios',
            name='id',
            field=models.UUIDField(default=uuid.UUID('5b4de644-4696-48e9-a7cb-5056705be0ce'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='userzt',
            name='fecha_nac',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='userzt',
            name='telefono',
            field=models.CharField(default='Telefono no asignado', max_length=18, null=True),
        ),
    ]