from django.db import models
from datetime import datetime

# Create your models here.
class bookingListItem(models.Model):
    user = models.CharField(max_length=100)
    content = models.TextField() 
    # due_date=models.DateField( null=True,blank=True)
    # show_datetime = models.TextField() 
    