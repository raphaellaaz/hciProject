# Generated by Django 4.2.3 on 2023-08-15 18:11

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('appHCI', '0011_alter_infosol_id_alter_solucion_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infosol',
            name='id',
            field=models.UUIDField(default=uuid.UUID('9a57d4ee-e8fa-4ccf-8eef-94953f6bc2ee'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='solucion',
            name='id',
            field=models.UUIDField(default=uuid.UUID('a72be3b9-cc1d-4a92-8d7d-0128c195eb3a'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='suscritos',
            name='id',
            field=models.UUIDField(default=uuid.UUID('0c93fafe-c6e1-4f30-b424-21fd8c9a6ce9'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='trabaja',
            name='id',
            field=models.UUIDField(default=uuid.UUID('2c312926-d722-4e3a-8e2c-7416be5fb91d'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='typeuser',
            name='id',
            field=models.UUIDField(default=uuid.UUID('f875969e-b89d-425b-b404-b6677a773ba9'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='u_negocios',
            name='id',
            field=models.UUIDField(default=uuid.UUID('c2a471f5-31bb-4883-8253-1bc884db2861'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='userzt',
            name='id',
            field=models.CharField(default=uuid.uuid4, editable=False, max_length=36, primary_key=True, serialize=False),
        ),
    ]