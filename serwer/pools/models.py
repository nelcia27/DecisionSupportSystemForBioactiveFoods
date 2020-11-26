from django.db import models

# Create your models here.


class Experiment(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=400)
    description = models.CharField(max_length=1500)
    link = models.CharField(max_length=600)
    author = models.CharField(max_length=300)
    create_date = models.DateTimeField(auto_now_add=True)
    number_of_measured_properties = models.PositiveIntegerField(default=1, blank=False)
    number_of_samples = models.PositiveIntegerField(default=1, blank=False)
    # foreign key product
    #list_samples_ids = models.
    def __str__(self):
        return self.name