from django.db import models

from courses.models import BaseClass

# Create your models here.

from django.contrib.auth.models import User


class Instructors(BaseClass):

    Profile = models.OneToOneField('authentication.Profile',on_delete=models.CASCADE)

    name = models.CharField(max_length=50)

    image = models.ImageField(upload_to='instructor-image/')

    description = models.TextField()

    def __str__(self):
        return self.name
    
    class Meta:

        verbose_name = 'Instructors' 

        verbose_name_plural = 'Instructors'