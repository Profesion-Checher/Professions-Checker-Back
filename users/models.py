from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager
from django.db import models

class ClientManager(BaseUserManager):
  def create_user(self, email, first_name, last_name, password=None, **extra_fields):
    if not email:
        raise ValueError('El correo es obligatorio')
    email = self.normalize_email(email)

    user = self.model(
        email=email,
        first_name=first_name,
        last_name=last_name,
        company=extra_fields.get('company'),
        profession=extra_fields.get('profession'),
        salary=extra_fields.get('salary'),
    )
    user.set_password(password)
    user.save(using=self._db)
    return user


  def create_superuser(self, email, first_name, last_name, password=None, **extra_fields):
    extra_fields.setdefault('is_staff', True)
    extra_fields.setdefault('is_superuser', True)

    return self.create_user(email, first_name, last_name, password, **extra_fields)

class Client(AbstractBaseUser, PermissionsMixin):
  email = models.EmailField(unique=True)
  first_name = models.CharField(max_length=100)
  last_name = models.CharField(max_length=100)
  company = models.CharField(max_length=100, blank=True, null=True)
  profession = models.CharField(max_length=100, blank=True, null=True)
  salary = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

  is_active = models.BooleanField(default=True)
  is_staff = models.BooleanField(default=False)

  objects = ClientManager()

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['first_name', 'last_name']

  def __str__(self):
    return f"{self.first_name} {self.last_name} ({self.email})"
