from django.core.validators import MaxValueValidator
from django.db import models


# Create your models here.
class Human(models.Model):
    name = models.CharField(verbose_name='Name', help_text='It is a name of a human.', max_length=200)
    age = models.PositiveSmallIntegerField(verbose_name='Age', help_text='How old is this human.', validators=[MaxValueValidator(150)])
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
