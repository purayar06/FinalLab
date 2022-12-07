from django.db import models
from datetime import datetime

# Create your models here.
class bookingListItem(models.Model):
    user = models.CharField(max_length=100)
    content = models.TextField(null=False) 
    showsdatetime = models.TextField(null=False) 
    