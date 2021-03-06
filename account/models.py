from django.db import models
from django.contrib.auth.models import AbstractUser,BaseUserManager
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class MyAccountManager(BaseUserManager):
    def create_user(self,email,username,name,password=None):
        if not email:
            raise ValueError("User's must an Email I'd")
        if not username:
            raise ValueError("User's must have an username")
        user=self.model(
            email=self.normalize_email(email),
            username=username,
            name=name,
        )
        user.set_password(password)
        user.save(using= self._db)
        return user

    def create_superuser(self,email,username,password,name,**extra_fields):
        user = self.create_user(
            email=self.normalize_email(email),
            password=password,
            username=username,
            name=name,
        )
        extra_fields.setdefault('is_admin',True)
        extra_fields.setdefault('is_staff',True)
        extra_fields.setdefault('is_superuser',True)
        user.save(using=self._db)
        return user

class Account(AbstractUser):
    email           = models.EmailField(verbose_name="email",unique=True)
    username        = models.CharField(max_length=30,unique=True)
    name            = models.CharField(max_length=250)
    date_joined     = models.DateTimeField(verbose_name="date joined",auto_now_add=True)
    last_login      = models.DateTimeField(verbose_name='last login',auto_now=True)
    is_admin        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=True)
    is_staff        = models.BooleanField(default=False)
    is_superuser    = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username','name']

    objects = MyAccountManager()
    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def  has_module_perms(self, app_label):
        return True

@receiver(post_save,sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender,instance=None,created=False,**kwargs):
    if created:
        Token.objects.create(user=instance)