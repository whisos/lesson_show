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

    # Перевірка пароля на відповідність вимогам
    def clean(self):
        super().clean()
        if len(self.password) < 8:
            raise ValidationError("Your password must contain at least 8 characters.")
        if self.password.isdigit():
            raise ValidationError("Your password can’t be entirely numeric.")
        if self.password.isalpha():
            raise ValidationError("Your password must contain at least one digit.")
        if self.password.islower() or self.password.isupper():
            raise ValidationError("Your password must contain both uppercase and lowercase letters.")
        if not any(char.isdigit() for char in self.password):
            raise ValidationError("Your password must contain at least one digit.")
        if not any(char.isupper() for char in self.password) or not any(char.islower() for char in self.password):
            raise ValidationError("Your password must contain both uppercase and lowercase letters.")
        if not any(char.isalnum() for char in self.password):
            raise ValidationError("Your password must contain at least one special character.")
        if self.password.lower() in ['password', '123456', 'qwerty']:
            raise ValidationError("Your password is too common.")
    
    def save(self, *args, **kwargs):
        if not self.id:  # Якщо це новий користувач
            self.set_password(self.password)  # Викликаємо set_password для створення хешу паролю
        self.full_clean()  # Перевірка на відповідність обмеженням перед збереженням
        
        # Перевіряємо, чи будь-які дані користувача були змінені
        if (
            'username' in kwargs or 'first_name' in kwargs or 'last_name' in kwargs or
            'email' in kwargs or 'role' in kwargs
        ):
            self.full_clean()  # Перевірка на відповідність обмеженням після зміни даних користувача

        super().save(*args, **kwargs)
        self.assign_role_permissions()  # Надаємо дозволи відповідно до ролі користувача


    def assign_role_permissions(self):
        if self.role == 'user':
            permissions = Permission.objects.filter(codename__in=['view_info'])
        elif self.role == 'moderator':
            permissions = Permission.objects.filter(codename__in=['add_object', 'change_object'])
        elif self.role == 'admin':
            permissions = Permission.objects.all()
        
        # Надає дозволи користувачеві
        self.user_permissions.set(permissions)

    def __str__(self):
        return self.username
