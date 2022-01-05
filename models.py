from django.db import models

# Create your models here.
class Truth(models.Model):
    Name=models.CharField(max_length=25)
    Address=models.TextField()

    def __str__(self):
        return self.Name


