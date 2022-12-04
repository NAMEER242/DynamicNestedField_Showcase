from django.db import models


class C(models.Model):
    charfield = models.CharField(max_length=100, null=True)

    def __str__(self):
        return self.charfield


class B(models.Model):
    charfield = models.CharField(max_length=100, null=True)
    c = models.ForeignKey(C, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.charfield


class A(models.Model):
    charfield = models.CharField(max_length=100, null=True)
    b = models.ManyToManyField(B)

    def __str__(self):
        return self.charfield
