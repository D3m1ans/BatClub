from django.db import models


# Create your models here.

class Card(models.Model):
    name = models.CharField('Имя', max_length=100)
    alterego = models.CharField('Альтер эго', max_length=100)
    debut = models.DateField('Год появления')
    gender = models.CharField('Пол', max_length=100)
    occupation = models.CharField('Позиция', max_length=100)
    description = models.TextField('Описание')
    skills = models.TextField('Способности')
    background = models.TextField('Предыстория')
    appearance = models.TextField('Внешность')
    alliess = models.TextField('Союзники')
    enemises = models.TextField('Враги')

    def __str__(self):
        return self.name
