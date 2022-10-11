from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, email, full_name ,password, **extra_fields):
        if not email:
            raise ValueError("The given email must be set")
        email = self.normalize_email(email)
        user = self.model(email=email, full_name=full_name, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, full_name, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_active", True)
        
        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser must have is_staff=True.")
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self.create_user(email, full_name,password, **extra_fields)

USER_ROLE = (
        ("Vendor", "Vendor"),
        ("Customer", "Customer")
    )
class User(AbstractBaseUser, PermissionsMixin):
    full_name = models.CharField("Full Name", max_length=255)
    email = models.EmailField("Email", unique=True)
    role = models.CharField("User Role", max_length=50, choices=USER_ROLE)
    is_active = models.BooleanField("Active", default=True)
    is_staff = models.BooleanField("Staff", default=False)
    is_superuser = models.BooleanField("Superuser", default=False)
    date_joined = models.DateTimeField(auto_now_add=True, null=True, blank=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['full_name']

    objects = UserManager()

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"
        ordering = ["-date_joined"]

    def __str_(self):
        return self.full_name