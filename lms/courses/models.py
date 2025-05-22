from django.db import models

import uuid


# Create your models here.
category_choice = [
    ('IT & Softwares','IT & Softwares'),
    ('Marketing','Marketing'),
    ('Finance','Finance'),
]

class LevelChoices(models.TextChoices):

    BEGINNER = 'beginner','beginner'

    INTERMEDIATE = 'intermediate', 'Intermediate'

    ADVANCED = 'Advanced', 'Advanced'


class Typechoices(models.TextChoices):

    FREE   = 'Free','Free'

    PREMINUM = 'Premium','Premium' 


class BaseClass(models.Model):
  

    # package used for slug
    uuid = models.SlugField(unique=True,default=uuid.uuid4)

    # soft deleteing
    active_status =models.BooleanField(default=True)


    created_at = models.DateTimeField(auto_now_add=True)


    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:

        abstract = True



    




class CategoryChoices(models.TextChoices):

    IT_SOFTWARES = 'IT & Softwares','IT & Softwares'
    
    FINANCE = 'Finance','Finance'

    MARKETING = 'Marketing','Marketing'

class Courses(BaseClass):

    title = models.CharField(max_length=50)

    description = models.TextField()

    image = models.ImageField(upload_to='course-images/')

                                #  appname.model name
    instructor = models.ForeignKey('instructors.instructors',on_delete=models.CASCADE)

    #category = models.CharField(max_length=25, choices =category_choice) # defining choices using list of tuples
    
    category = models.CharField(max_length=25, choices =CategoryChoices.choices) # defining using class CategoryChoice


    level = models.CharField(max_length=25,choices=LevelChoices.choices)

    type = models.CharField(max_length=15,choices=Typechoices.choices)

    fees = models.DecimalField(max_digits=8, decimal_places=2)

    offer_fee = models.DecimalField(max_digits=8, decimal_places=2, null=True,blank=True)


    def __str__(self):
        return f'{self.title}--{self.instructor}'
    

    class Meta:

      verbose_name = 'Courses'

      verbose_name_plural = 'Courses'    

      ordering =['id']