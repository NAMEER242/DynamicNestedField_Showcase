from django.db import models


class C(models.Model):
    charfield = models.CharField(max_length=100)


class B(models.Model):
    charfield = models.CharField(max_length=100)
    c = models.ForeignKey(C, on_delete=models.CASCADE, null=True, blank=True)


class A(models.Model):
    charfield = models.CharField(max_length=100)
    b = models.ManyToManyField(B)

