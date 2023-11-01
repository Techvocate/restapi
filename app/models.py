from django.db import models

"""class Legalease(models.Model):
    prompt = models.CharField(max_length=100)
    result = models.CharField(max_length=700)
"""

class Item(models.Model):
    name=models.CharField(max_length=200)
    created=models.DateTimeField(auto_now_add=True)