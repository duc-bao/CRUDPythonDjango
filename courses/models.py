from django.db import models
from  django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    avatar = models.ImageField(upload_to='/uploads/%Y/%m')
# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100, nullable=False, unique=True)