from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import AbstractUser, User
from django.db import models

# Create your models here.

# class User(AbstractUser):
#     birth_date = models.DateField(null=True, blank=True)