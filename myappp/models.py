from django.db import models

# Create your models here.
class userregister(models.Model):
    GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female'),
    )
    
    username = models.CharField(max_length=30, blank=True, null=True)
    firstname = models.CharField(max_length=30, blank=True, null=True)
    lastname = models.CharField(max_length=30, blank=True, null=True)
    email = models.CharField(max_length=30)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    phone_number = models.CharField(max_length=12, blank=True, null=True)

    def __str__(self):
        return self.firstname+" "+self.lastname