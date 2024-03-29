# Generated by Django 4.2.3 on 2023-07-27 23:42

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('appHCI', '0005_alter_infosol_id_alter_solucion_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='u_negocios',
            name='departamento',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='u_negocios',
            name='email_negocios',
            field=models.CharField(max_length=40, null=True),
        ),
        migrations.AddField(
            model_name='u_negocios',
            name='piso',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='infosol',
            name='id',
            field=models.UUIDField(default=uuid.UUID('ba5da8e5-c68d-4924-86b5-7c8ce7aa11bb'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='solucion',
            name='id',
            field=models.UUIDField(default=uuid.UUID('ee62c590-ad08-4d41-a3b5-a8b6701a27f6'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='suscritos',
            name='id',
            field=models.UUIDField(default=uuid.UUID('2907d66a-87b7-413a-bace-842e9576f630'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='trabaja',
            name='id',
            field=models.UUIDField(default=uuid.UUID('a80c4ef9-2e96-4414-870b-becd570edbe4'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='typeuser',
            name='id',
            field=models.UUIDField(default=uuid.UUID('77ef796b-2ea3-4c7f-aa95-43c0aee4b0d0'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='u_negocios',
            name='id',
            field=models.UUIDField(default=uuid.UUID('5332b502-1ee3-49d4-b06a-83c6a676174d'), editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='userzt',
            name='id',
            field=models.UUIDField(default=uuid.UUID('20133a58-e866-4846-8bbc-e31b5209c937'), editable=False, primary_key=True, serialize=False),
        ),
    ]
