from django.db import models
from django.contrib.auth.models import User

class Contact(models.Model):
    name = models.CharField(max_length=150)
    first_name = models.CharField(max_length=150)
    email = models.CharField(max_length=150,null=True,blank=True)
    phone = models.CharField(max_length=150)
    date_enregistrement = models.DateTimeField(auto_now_add=True)
    auteur = models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.first_name} {self.name}"