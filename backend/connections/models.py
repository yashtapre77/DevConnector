from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import BaseUserManager

# Create your models here.


class UserManager(BaseUserManager):
    """Helps Django work with our custom user model"""

    use_in_migrations = True

    def create_user(self, name, email, password=None):
        """Creates a new user profile objects"""

        if not email:
            raise ValueError('Users must have an email address')

        if not name:
            raise ValueError('Users must have names')

        email = self.normalize_email(email)
        name = name.strip()
        user = self.model(name=name, email=email)
        user.set_password(password)
        user.save(using=self._db)

        return user