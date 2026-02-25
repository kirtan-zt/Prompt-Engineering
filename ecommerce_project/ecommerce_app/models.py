from django.db import models
from django.core.validators import RegexValidator, MinValueValidator

class Product(models.Model):
    name = models.CharField(
        max_length=100,
        validators=[
            RegexValidator(
                r'^[a-zA-Z0-9\s-]*$',
                'Only alphanumeric characters, spaces, and hyphens are allowed.'
            )
        ]
    )
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0.01)]
    )
    stock = models.IntegerField(validators=[MinValueValidator(1)])
    category = models.CharField(
        max_length=100,
        validators=[
            RegexValidator(
                r'^[a-zA-Z0-9\s-]*$',
                'Only alphanumeric characters, spaces, and hyphens are allowed.'
            )
        ]
    )

    def __str__(self):
        return self.name
