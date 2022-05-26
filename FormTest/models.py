from django.db import models

# Create your models here.

class CartoonEntry(models.Model):
    cartoon_name = models.CharField(max_length=100)
    episode_count = models.IntegerField()
    date_finished = models.DateTimeField()
    rating = models.DecimalField(max_digits = 2, decimal_places = 1)

    def __str__(self):
        return self.cartoon_name
