from django.db import models

# Create your models here.
class soft(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    email=models.EmailField()
    department=models.CharField(max_length=100)
    disignation=models.CharField(max_length=100)
    dateofjoin=models.DateField()
    salery=models.CharField(max_length=100)
    photo=models.ImageField(upload_to='image/')
    def __str__(self):
        return self.firstname
    

