from django.db import models
from django.contrib.auth.models import User
from datetime import date

class Profession(models.Model):
    profession_name = models.CharField(max_length=100, unique=True)
    current_salary = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    future_salaries = models.JSONField(default=list)

    def __str__(self):
        return self.profession_name

class Profile(models.Model):
    #Estas listas funcionan de tal manera que el formulario los que estan en mayusculas son el nombre del <option> y lo que esta en mi nuscula es el valor
    
    PREFERENCES = [
        ('MASTER','Master'),
        ('CAREER','Career'),
    ]
    GENERO_CHOICES = [
        ('MALE', 'Male'),
        ('FEMALE', 'Female'),
        ('PREFER_NOT_TO_SAY', 'Prefer Not to Say'),
    ]

    User = models.OneToOneField(User, on_delete=models.CASCADE)
    Name = models.TextField(default=None)
    Last_name = models.TextField(default='', null=True)
    birth_Date = models.DateField(default=None)
    def calcular_edad(self):
        today = date.today()
        edad = today.year - self.birth_date.year - ((today.month, today.day) < (self.birth_date.month, self.birth_date.day))
        return edad

    Edad = property(calcular_edad)
    Preferences = models.CharField(max_length=21, choices=PREFERENCES, default='MASTER')
    Gender = models.CharField(max_length=20, choices=GENERO_CHOICES, default='PREFER_NOT_TO_SAY')


    def __str__(self):
        return self.user.username