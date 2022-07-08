from django.db import models

class test(models.Model):
    time = models.DateTimeField(minute=0, second=0)

