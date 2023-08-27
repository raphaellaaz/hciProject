# Generated by Django 4.2.3 on 2023-08-27 06:45

from django.db import migrations, models
import shortuuid.main
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('appHCI', '0010_alter_infosol_id_alter_solucion_cod_solution_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infosol',
            name='id',
            field=models.CharField(default=uuid.UUID('db8c585e-1722-44af-b557-3f9fab21b7d8'), editable=False, max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='solucion',
            name='cod_solution',
            field=models.CharField(default=shortuuid.main.ShortUUID.uuid, max_length=7, unique=True),
        ),
        migrations.AlterField(
            model_name='solucion',
            name='id',
            field=models.CharField(default=uuid.UUID('2b664e27-c91b-4c66-922f-39e7106732f6'), editable=False, max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='suscritos',
            name='id',
            field=models.CharField(default=uuid.UUID('d5392d57-8acc-4be9-b95b-a53509ef2861'), editable=False, max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='trabaja',
            name='id',
            field=models.CharField(default=uuid.UUID('56aa4979-218b-494e-b3e2-57538d513c82'), editable=False, max_length=36, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='typeuser',
            name='id',
            field=models.CharField(default=uuid.UUID('b5e5101f-21cd-4929-a37b-3f0428a8c0f4'), editable=False, max_length=36, primary_key=True, serialize=False),
        ),
    ]
