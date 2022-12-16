from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator


class Item(models.Model):
    picture = models.ImageField(null=True, blank=True, editable=True, upload_to='images/')
    name = models.CharField(max_length=40, validators=[MinLengthValidator(2, 'Занадто мале значеня'), MaxLengthValidator(40, 'Занадто велике значеня')])
    about_item = models.TextField(blank=True, max_length=600)
    price = models.FloatField(default=0, blank=False)

    def __str__(self):
        return self.name




