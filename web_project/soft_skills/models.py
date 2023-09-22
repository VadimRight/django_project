from django.db import models


class Articles(models.Model):
    title = models.CharField('Характеристика', max_length= 50)
    description = models.CharField('Описание', max_length= 250)

    def __str__(self):
        return self.title