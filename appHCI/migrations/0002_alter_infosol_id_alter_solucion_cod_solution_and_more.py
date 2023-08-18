# Generated by Django 4.2.3 on 2023-08-18 19:06

from django.db import migrations, models
import shortuuid.main
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('appHCI', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='infosol',
            name='id',
            field=models.UUIDField(default=uuid.UUID('763c5874-ecd1-4f45-bbab-6f5af5334a2b'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='solucion',
            name='cod_solution',
            field=models.CharField(default=shortuuid.main.ShortUUID.uuid, max_length=7, unique=True),
        ),
        migrations.AlterField(
            model_name='solucion',
            name='id',
            field=models.UUIDField(default=uuid.UUID('336ef8dc-e7c4-41a2-9bf6-e6c8dbb39b58'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='suscritos',
            name='id',
            field=models.UUIDField(default=uuid.UUID('27cede65-0764-4623-91fb-90f93fa2dc24'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='trabaja',
            name='id',
            field=models.UUIDField(default=uuid.UUID('b2026258-fbe2-427f-bf4e-087b2adbc6c1'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='typeuser',
            name='id',
            field=models.IntegerField(default=uuid.UUID('a77759ce-e5fc-4a04-ad8c-5bdca3b7224f'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='u_negocios',
            name='id',
            field=models.IntegerField(default=uuid.UUID('d1b410cb-29f4-4708-8385-78f27bbfcac6'), editable=False, primary_key=True, serialize=False),
        ),
    ]