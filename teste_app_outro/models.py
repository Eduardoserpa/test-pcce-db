from django.db import models
from decouple import config

# Create your models here.
class TestUserTypeOutroModel(models.Model):
    id = models.SmallAutoField(primary_key=True)
    type_outro = models.CharField(unique=True)
    description_outro = models.CharField()

    class Meta:
        db_table = f'{config("DB_SCHEMA_TEST_APP")}\".\"test_user_type_outro'
        ordering = ["id", ]

class TestUserOutroModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    name_outro = models.CharField()
    email_outro = models.CharField(unique=True)
    password_outro = models.CharField()

    class Meta:
        db_table = f'{config("DB_SCHEMA_TEST_APP")}\".\"test_user_outro'
        ordering = ["id", ]
