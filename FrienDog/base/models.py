from django.db import models
from django.contrib.auth.models import User



class Profile(models.Model):
    name = models.CharField(max_length=100)
    year_of_birth = models.IntegerField(null=True)
    GENDER_CHOICES = [
        ('male', 'Male'),
        ('female', 'Female'),
    ]
    gender = models.CharField(max_length=6, choices=GENDER_CHOICES, null=True)
    dog_name = models.CharField(max_length=100, null=True)
    DOG_SIZE_CHOICES = [
        ('small', 'Small'),
        ('big', 'Big'),
    ]
    dog_size = models.CharField(max_length=5, choices=DOG_SIZE_CHOICES, null=True)
    dog_breed = models.CharField(max_length=100, null=True)
    occupation = models.TextField(null=True)
    hobbies = models.TextField(null=True)


    def __str__(self):
        return self.name
