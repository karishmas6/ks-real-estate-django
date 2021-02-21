from django.db import models
from datetime import datetime

class Realtor(models.Model):
    
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='photos/%Y/%m%d/')
    description = models.TextField(blank=True)
    email = models.CharField(max_length=30)
    hire_date = models.DateTimeField(default=datetime.now , blank = True)
    is_mvp = models.BooleanField(default=False)
    phone = models.CharField(max_length=15)

    # Function to return main field which we are considering to be name
    def __str__(self):
        return self.name


