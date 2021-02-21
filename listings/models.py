from django.db import models
from datetime import datetime
from realtors.models import Realtor


class Listing(models.Model):

    realtor = models.ForeignKey(Realtor , on_delete=models.DO_NOTHING) # Foreign key from Realtor table
    title = models.CharField(max_length=200)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=20)
    description = models.TextField(blank=True)
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    bathrooms = models.DecimalField(max_digits=2,decimal_places=1)
    sqft = models.IntegerField()
    garage = models.IntegerField(default=0)
    lot_size = models.DecimalField(max_digits=5 , decimal_places=1)
    list_date = models.DateTimeField(default=datetime.now ,blank = True)
    is_published = models.BooleanField(default=True)
    
    main_image = models.ImageField(upload_to='photos/%Y/%m%d/')
    image1 = models.ImageField(upload_to='photos/%Y/%m%d/',blank = True)
    image2 = models.ImageField(upload_to='photos/%Y/%m%d/',blank = True)
    image3 = models.ImageField(upload_to='photos/%Y/%m%d/',blank = True)
    image4 = models.ImageField(upload_to='photos/%Y/%m%d/',blank = True)
    image5 = models.ImageField(upload_to='photos/%Y/%m%d/',blank = True)
    image6 = models.ImageField(upload_to='photos/%Y/%m%d/',blank = True)

    # Function to return main field which we are considering to be title
    def __str__(self):
        return self.title