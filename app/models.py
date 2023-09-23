from django.db import models

class Legalease(models.Model):
    prompt = models.CharField(max_length=100)
    result = models.CharField(max_length=700)
