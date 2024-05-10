from django.db import models

from django.contrib.auth.models import AbstractUser
from django.core.exceptions import ValidationError
from django.contrib.auth.models import Permission

# Create your models here.

class CustomUser(AbstractUser):
    password = models.CharField(max_length=128)
    
    # Ролі
    role = models.CharField(max_length=20, choices=(
        ('user', 'User'),
        ('moderator', 'Moderator'),
        ('admin', 'Administrator'),
    ), default='user')
  
    # Треба
    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='customuser_set',
        related_query_name='user'
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='customuser_set',
        related_query_name='user'
    )

    # Перевірки
    def clean(self):
        super().clean()
        # Перевірка пароля на відповідність вимогам
        if len(self.password) < 8:
            raise ValidationError("Your password must contain at least 8 characters.")
        if self.password.isdigit():
            raise ValidationError("Your password can’t be entirely numeric.")
    
    def save(self, *args, **kwargs):
        if not self.id:  # Якщо це новий користувач
            self.set_password(self.password)  # Викликаємо set_password для створення хешу паролю
        self.full_clean()  # Перевірка на відповідність обмеженням перед збереженням
        super().save(*args, **kwargs)
        self.assign_role_permissions()  # Надаємо дозволи відповідно до ролі користувача
          
    def __str__(self):
        return self.username
    
    def assign_role_permissions(self):
        # Отримайте або створіть дозволи для поточного користувача на основі його ролі
        if self.role == 'user':
            permissions = Permission.objects.filter(codename__in=['view_info'])
        elif self.role == 'moderator':
            permissions = Permission.objects.filter(codename__in=['add_object', 'change_object'])
        elif self.role == 'admin':
            permissions = Permission.objects.all()
        
        # Надайте дозволи користувачеві
        self.user_permissions.set(permissions)
