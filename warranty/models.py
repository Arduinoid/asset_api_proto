from django.db import models


class Server(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    make = models.CharField(max_length=50)
    model = models.CharField(max_length=50)
    serial = models.CharField(max_length=50)

    class Meta:
        ordering = ('created',)

