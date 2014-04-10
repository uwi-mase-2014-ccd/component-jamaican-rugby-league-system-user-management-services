from django.db import models


class User(models.Model):
    firstname = models.CharField(max_length=25)
    lastname = models.CharField(max_length=30)
    email = models.EmailField(help_text= "eg. email@gmail.com")
    dateOfBirth = models.DateField(help_text= 'format : YYYY-MM-DD')
    username = models.CharField(max_length=100, primary_key=True, help_text= 'This is the primary key')
    password = models.CharField(max_length=30)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES,help_text= "accepts ")
    usertype = models.CharField(max_length=25)