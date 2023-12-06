from django.db import models
import psutil

# Create your models here.

class Processes(models.Model):
        process_list=models.CharField(max_length=2000)

        process_list = "asdf"

        def __str__(self):
            return self.process_list

