from django.db import models

# Create your models here.
class Query(models.Model):
    query = models.TextField()

    def __str__(self):
        return self.query[0:50]
