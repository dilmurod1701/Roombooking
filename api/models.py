from django.db import models

# Create your models here.


class Room(models.Model):
    name = models.CharField(max_length=100)
    xona = models.IntegerField()
    booked = models.BooleanField(default=False)
    start = models.DateTimeField(null=True, blank=True)
    end = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.name
