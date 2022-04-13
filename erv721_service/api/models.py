from django.db import models


class Token(models.Model):
    """Token's model
    id - primary key
    unique_hash - уникальный хэш
    tx_hash - хэш транзакции создания токена
    media_url - урл с произвольным изображением
    owner - адрес пользователя в сети Ethereum"""
    id = models.CharField(max_length=20, primary_key=True)
    unique_hash = models.CharField(max_length=20, unique=True)
    tx_hash = models.CharField(max_length=34, unique=True)
    media_url = models.URLField
    owner = models.URLField
# Create your models here.
