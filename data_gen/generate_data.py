import random
from datetime import datetime, timedelta
from django.core.management.base import BaseCommand
from django.utils import timezone
from django.contrib.auth import get_user_model
from faker import Faker
from shortuuid import uuid
from appHCI.models import TypeUser, U_Negocios, TypeSol, EstadoSol, InfoSol, Solucion, Suscritos, Trabaja

User = get_user_model()
fake = Faker()

class Command(BaseCommand):
    help = 'Generates random data for testing purposes'

    def handle(self, *args, **kwargs):
        self.generate_type_users()
        self.generate_users()
        self.generate_u_negocios()
        self.generate_type_sols()
        self.generate_estado_sols()
        self.generate_info_sols()
        self.generate_soluciones()
        self.generate_suscritos()
        self.generate_trabaja()
        self.stdout.write(self.style.SUCCESS('Data generated successfully'))

    def generate_type_users(self):
        type_user_names = ['Admin', 'Usuario', 'Invitado']
        for name in type_user_names:
            TypeUser.objects.create(typeU=name)

    def generate_users(self):
        for _ in range(10):
            ci_user = random.randint(10000, 99999)
            cargo = random.choice(['Gerente', 'Analista', 'Desarrollador'])
            email = fake.email()
            telefono = fake.phone_number()
            fecha_nac = fake.date_of_birth(minimum_age=20, maximum_age=50)
            tipo_U = random.choice(TypeUser.objects.all())
            User.objects.create_user(username=f'user_{ci_user}', ci_user=ci_user, cargo=cargo, email=email, telefono=telefono, fecha_nac=fecha_nac, tipo_U=tipo_U)

    def generate_u_negocios(self):
        for _ in range(5):
            departamento = fake.word()
            email_negocios = f'{departamento.lower()}@negocios.com'
            telef_negocios = fake.phone_number()
            U_Negocios.objects.create(departamento=departamento, email_negocios=email_negocios, telef_negocios=telef_negocios)

    def generate_type_sols(self):
        type_sol_names = ['Soporte', 'Desarrollo', 'Consulta']
        for name in type_sol_names:
            TypeSol.objects.create(tipoSol=name, descripcion_tipo_sol=f'Descripción de {name}')

    def generate_estado_sols(self):
        estado_sol_names = ['Pendiente', 'En Progreso', 'Completado']
        for name in estado_sol_names:
            EstadoSol.objects.create(estado_proj=name)

    def generate_info_sols(self):
        for _ in range(10):
            id_sol = random.choice(TypeSol.objects.all())
            descriptioSol = f'Descripción de la solución {id_sol}'
            id_esta = random.choice(EstadoSol.objects.all())
            fecha_propuesto = timezone.now() - timedelta(days=random.randint(0, 30))
            fecha_comienzo = fecha_propuesto + timedelta(days=random.randint(1, 10))
            fecha_culminado = fecha_comienzo + timedelta(days=random.randint(1, 20))
            InfoSol.objects.create(id_sol=id_sol, descriptioSol=descriptioSol, id_esta=id_esta, fecha_propuesto=fecha_propuesto, fecha_comienzo=fecha_comienzo, fecha_culminado=fecha_culminado)

    def generate_soluciones(self):
        for _ in range(10):
            cod_solution = uuid()
            nombreSol = f'Solución {cod_solution}'
            negocios_resp = random.choice(U_Negocios.objects.all())
            coordinador_sol = random.choice(User.objects.all())
            info_sol = random.choice(InfoSol.objects.all())
            Solucion.objects.create(cod_solution=cod_solution, nombreSol=nombreSol, negocios_resp=negocios_resp, coordinador_sol=coordinador_sol, info_sol=info_sol)

    def generate_suscritos(self):
        for _ in range(20):
            id_user = random.choice(User.objects.all())
            id_solution = random.choice(Solucion.objects.all())
            fecha_sus = timezone.now() - timedelta(days=random.randint(0, 30))
            Suscritos.objects.create(id_user=id_user, id_solution=id_solution, fecha_sus=fecha_sus)

    def generate_trabaja(self):
        for _ in range(20):
            id_user = random.choice(User.objects.all())
            id_solution = random.choice(Solucion.objects.all())
            descripcion_cargo = f'Descripción del cargo para {id_user}'
            cargo = random.choice(['Gerente', 'Analista', 'Desarrollador'])
            ingreso_cargo = timezone.now() - timedelta(days=random.randint(0, 365))
            Trabaja.objects.create(id_user=id_user, id_solution=id_solution, descripcion_cargo=descripcion_cargo, cargo=cargo, ingreso_cargo=ingreso_cargo)
