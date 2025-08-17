from django.db import models



class Material(models.Model):
 
  idMaterial = models.AutoField(primary_key=True)  
  descripcion = models.CharField(max_length=255)
  proceso = models.TextField(max_length=500)
  

# Create your models here.
