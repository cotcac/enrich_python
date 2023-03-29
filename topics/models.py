from django.db import models

class Topics(models.Model):
    title = models.CharField(max_length=50)