from django.core.validators import MaxValueValidator
from django.db import models


class ColorsChoices(models.TextChoices):
    BLACK = 'black', 'Black'
    WHITE = 'white', 'White'
    RED = 'red', 'Red'


class Color(models.Model):
    name = models.CharField(verbose_name='Name', help_text='The name of the color.', max_length=32)

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"<Color - {self.name}>"


class Human(models.Model):
    name = models.CharField(verbose_name='Name', help_text='It is a name of a human.', max_length=200)
    age = models.PositiveSmallIntegerField(verbose_name='Age', help_text='How old is this human.', validators=[MaxValueValidator(150)])

    favourite_color = models.CharField(
        verbose_name='Favourite color',
        max_length=32,
        choices=ColorsChoices.choices,
        default=ColorsChoices.WHITE)

    favourite_color_by_foreign_key = models.ForeignKey(
        to=Color,
        related_name='humans_related_by_foreign_key',
        on_delete=models.SET_NULL,
        null=True,
        blank=True)

    favourite_color_many_to_many = models.ManyToManyField(
        to=Color,
        related_name='human_related_by_many_to_many'
    )

    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.age}"

    def __repr__(self):
        return f"<Human (name:{self.name}, age:{self.age})>"


class SuperHuman(Human):
    level = models.PositiveIntegerField(
        verbose_name='Level',
        help_text='Level of power.'
    )

    def __str__(self):
        return f"{self.name} - {self.age}"

    def __repr__(self):
        return f"<SuperHuman (name:{self.name}, age:{self.age})>"