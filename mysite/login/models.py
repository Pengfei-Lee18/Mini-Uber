from django.db import models
from datetime import date

# Create your models here.

class User(models.Model):

    gender = (
        ('male', "M"),
        ('female', "F"),
    )

    name = models.CharField(max_length=128, unique=True)
    password = models.CharField(max_length=256)
    email = models.EmailField(unique=True)
    sex = models.CharField(max_length=32, choices=gender, default="M")
    driver = models.BooleanField(default=False)
    c_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["-c_time"]
        verbose_name = "user"
        verbose_name_plural = "user"
    
class Car(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    cartype = models.CharField(max_length=128, unique=True)
    plateNumber = models.CharField(max_length=256)
    passengersNumber = models.DecimalField(max_digits=3, decimal_places=0)
    freeText = models.CharField(max_length=256)
    def __str__(self):
        return self.plateNumber

class Ride(models.Model):
    owner = models.ForeignKey(User, related_name = "owner", on_delete=models.CASCADE)
    ownernumber = models.DecimalField(max_digits=3, decimal_places=0)
    cartype = models.CharField(max_length=256)
    ridedriver = models.CharField(max_length=128)
    sharer = models.ManyToManyField(User, through='Relationship')
    dest = models.CharField(max_length=256)
    arrivaltime = models.DateTimeField()
    endtime = models.DateTimeField()
    share = models.BooleanField(default=False)
    freeText = models.CharField(max_length=256)
    status = models.DecimalField(max_digits=2, decimal_places=0)
    carspace = models.DecimalField(max_digits=3, decimal_places=0)
    def __str__(self):
        return self.owner.name +" "+self.dest

class Relationship(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ride = models.ForeignKey(Ride, on_delete=models.CASCADE)
    groupnumber = models.DecimalField(max_digits=3, decimal_places=0)
    