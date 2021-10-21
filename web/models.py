from django.db import models

class Pet(models.Model):
    name = models.CharField(max_length=255, null=False, blank=False)
    species = models.CharField(max_length=255, null=False, blank=False)
    age = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.name