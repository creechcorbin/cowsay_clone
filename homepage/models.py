from django.db import models


class UserInput(models.Model):
    text = models.CharField(max_length=100)