from django.db import models
from django.contrib.auth.models import AbstractUser
from django.apps import AppConfig


class User(AbstractUser):
    pass

class Lead(models.Model):
    first_name = models.CharField(max_length=20, verbose_name="Adı")
    last_name = models.CharField(max_length=20, verbose_name="Soyadı")
    age = models.IntegerField(default=0 ,verbose_name="Yaşı")
    agent = models.ForeignKey("Agent", on_delete=models.SET_NULL, null=True, verbose_name="Temsilci")

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    class Meta:
        verbose_name = ('Müşteri')
        verbose_name_plural = ('Müşteriler')

class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="Kullanıcı Adı")

    def __str__(self):
        return self.user.email
    
    class Meta:
        verbose_name = ('Temsilci')
        verbose_name_plural = ('Temsilciler')