from django.db import models

class Vehiculo(models.Model):
    idVehiculo = models.AutoField(primary_key=True)
    patente = models.CharField(max_length=10, unique=True)
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    dueno = models.CharField(max_length=100)
    rut = models.CharField(max_length=12)

    
class Estacionamiento(models.Model):
    idEstacionamiento = models.AutoField(primary_key=True)
    direccion = models.CharField(max_length=200)
    encargado = models.CharField(max_length=100)

class Ubicacion(models.Model):
    idUbicacion = models.AutoField(primary_key=True)
    numero = models.IntegerField()
    espacio = models.DecimalField(max_digits=8, decimal_places=2)
    estacionamiento = models.ForeignKey(Estacionamiento,on_delete=models.CASCADE,related_name="ubicaciones")

class Utiliza(models.Model):
    idUtiliza = models.AutoField(primary_key=True)
    vehiculo = models.ForeignKey(Vehiculo, on_delete=models.CASCADE,related_name="utilizaciones")
    estacionamiento = models.ForeignKey(Estacionamiento,on_delete=models.CASCADE,related_name="utilizaciones")
    ubicacion = models.ForeignKey(Ubicacion,on_delete=models.CASCADE,related_name="utilizaciones")
    inicio = models.DurationField()
    fin = models.DateTimeField(null=True, blank=True)
    costo = models.DateTimeField(max_digits=10, decimal_places=2)








