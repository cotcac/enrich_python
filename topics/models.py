from django.db import models

class Topics(models.Model):
    name = models.CharField(max_length=50)