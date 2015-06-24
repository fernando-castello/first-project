from django.db import models
class Email(models.Model):
    email = models.CharField(max_length=70, unique=True)

    def __unicode__(self):  #For Python 2, use __str__ on Python 3
        return self.email

        
