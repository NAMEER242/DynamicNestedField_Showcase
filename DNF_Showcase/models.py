from django.db import models
from pyasn1.compat.octets import null


class C(models.Model):
    charfield = models.CharField(max_length=100, null=True)


class B(models.Model):
    charfield = models.CharField(max_length=100, null=True)
    c = models.ForeignKey(C, on_delete=models.CASCADE, null=True, blank=True)


class A(models.Model):
    charfield = models.CharField(max_length=100, null=True)
    b = models.ManyToManyField(B)

