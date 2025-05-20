from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=100)
    registerd_at = models.DateField()

    objects = models.Manager()

    def __str__(self):
        return f"{self.name} ({self.registerd_at})"
