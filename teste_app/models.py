from django.db import models
from decouple import config

# Create your models here.
class TestUserTypeModel(models.Model):
    id = models.SmallAutoField(primary_key=True)
    type = models.CharField(unique=True)
    description = models.CharField()

    class Meta:
        db_table = f'{config("DB_SCHEMA_TEST_APP")}\".\"test_user_type'
        ordering = ["id", ]

class TestUserModel(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField()
    email = models.CharField(unique=True)
    password = models.CharField()

    class Meta:
        db_table = f'{config("DB_SCHEMA_TEST_APP")}\".\"test_user'
        ordering = ["id", ]
