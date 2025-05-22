from django.db import models

# Create your models here.

from courses.models import BaseClass


class QualifucationChoices(models.TextChoices):

    MATRICULATION = 'Matriculation','Matriculation'

    POST_MATRICULATION = 'post Matriculation','post Matriculation'

    DIPLOMA = 'Diploma','Diploma'

    GRADUATE = 'Graduate','Graduate'

    POST_GRADUATE = 'post Graduate','post Graduate'


    PHD = 'PHD','PHD'



class Students(BaseClass):

    profile = models.ForeignKey('authentication.Profile',on_delete=models.Case)

    name = models.CharField(max_length=50)

    image = models.ImageField(upload_to='student-images/')

    qualification = models.CharField(max_length=50,choices=QualifucationChoices.choices)


    def __str__(self):
        return self.name
    

    class Meta :

        verbose_name = 'student'

        verbose_name_plural = 'student'