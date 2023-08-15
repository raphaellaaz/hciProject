from django.db import models
#from login.models import Ulogin
import uuid
from django.contrib.auth.models import AbstractUser

#TODO -Añadir campos para manejar las rutas de los archivos(imagenes, pdfs)


class TypeUser(models.Model):
    id=models.IntegerField(default=uuid.uuid4(), editable=False, primary_key=True, null=False)
    typeU=models.CharField(max_length=15,default='Invitado', editable=True, null=False)

    def __str__(self):
        return self.typeU
    
class UserZT(AbstractUser):
    id=models.CharField(default=uuid.uuid4,max_length=36, editable=False, primary_key=True, null=False)
    ci_user=models.IntegerField(null=False, editable=True)
    fecha_nac=models.DateField(null=False, editable=True )
    email=models.CharField(max_length=40, default='Email no asignado', null=False, editable=True)
    telefono=models.CharField(max_length=18, default='Telefono no asignado', null=False, editable=True)
    tipo_U=models.ForeignKey(TypeUser, on_delete=models.CASCADE, related_name='R_TipoUser')

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='access_users'
    )

    # Define el campo 'user_permissions' con related_name personalizado
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='access_users'
    )
    def __str__(self):
        return self.ci_user

    
class U_Negocios(models.Model):
    id=models.UUIDField(default=uuid.uuid4(), editable=False, primary_key=True, null=False)
    departamento=models.CharField(max_length=30, editable=True, null=True)
    piso=models.CharField(max_length=10, null=True, editable=True)
    email_negocios=models.CharField(max_length=40, null=True, editable=True)
    telef_negocios=models.CharField(max_length=18, editable=True, null=False)

    def __str__(self):
        return 'Negocios: '+self.departamento
    
class TypeSol(models.Model):
    tipoSol=models.CharField(max_length=30, null=False, editable=True)
    descripcion_tipo_sol=models.TextField(max_length=300, null=False, editable=True)

    def __str__(self):
        return 'Tipo_'+self.tipoProj

class EstadoSol(models.Model):
    estado_proj=models.CharField(max_length=30, null=False, editable=True)

class InfoSol(models.Model):
    id=id=models.UUIDField(default=uuid.uuid4(), editable=False, primary_key=True, null=False)
    id_sol=models.ForeignKey(TypeSol, on_delete=models.CASCADE, related_name='R_TypeSol_Info')
    id_esta=models.ForeignKey(EstadoSol, on_delete=models.DO_NOTHING, related_name='R_Estado_Info')
    latest_mod=models.DateTimeField(null=False, editable=True)

class Solucion(models.Model):
     id=models.UUIDField(default=uuid.uuid4(), editable=False, primary_key=True, null=False)
     cod_solution=models.IntegerField(null=False, editable=False)
     nombreSol=models.TextField(max_length=300, editable=True, null=False)
     fecha_propuesto=models.DateField(null=False)
     fecha_comienzo=models.DateField(null=False, editable=True)
     fecha_culminado=models.DateField(null=True, editable=True)
     negocios_resp=models.ForeignKey(U_Negocios, on_delete=models.DO_NOTHING, related_name='R_Negocios_Sol')
     coordinador_sol=models.ForeignKey(UserZT, on_delete=models.DO_NOTHING, related_name='R_Coordinador_Sol')
     info_sol=models.ForeignKey(InfoSol, on_delete=models.DO_NOTHING, related_name='R_Info_Sol')
    
class Suscritos(models.Model):
    id=models.UUIDField(default=uuid.uuid4(), editable=False, primary_key=True, null=False)
    id_user=models.ForeignKey(UserZT, on_delete=models.DO_NOTHING, related_name='R_UserZT_Suscrit')
    id_solution=models.ForeignKey(Solucion, on_delete=models.CASCADE, related_name='R_Solution_Suscrit')
    fecha_sus=models.DateField(null=False, editable=False)

    def __str__(self):
        return 'Suscrito_'+id

class Trabaja(models.Model):
    id=models.UUIDField(default=uuid.uuid4(), editable=False, primary_key=True, null=False)
    id_user=models.ForeignKey(UserZT, on_delete=models.DO_NOTHING, related_name='R_UserZT_Trab')
    id_solution=models.ForeignKey(Solucion, on_delete=models.CASCADE, related_name='R_Solution_Trab')
    descripcion_cargo=models.TextField(max_length=120, null=False, editable=True)
    cargo=models.CharField(max_length=30, editable=True, null=False)
    ingreso_cargo=models.DateField(null=False)

    def __str__(self):
        return 'Trabajo_'+id

