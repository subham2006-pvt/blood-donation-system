from django.db import models
from django.contrib.auth.models import User


class Donor(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    gender = models.CharField(max_length=10)
    blood_group = models.CharField(max_length=5)
    phone = models.CharField(max_length=15)
    city = models.CharField(max_length=50)
    last_donation = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} - {self.blood_group}"


class BloodRequest(models.Model):
    patient_name = models.CharField(max_length=100)
    blood_group = models.CharField(max_length=5)
    hospital = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.patient_name
