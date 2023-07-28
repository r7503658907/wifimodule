from django.db import models

class wifiMode(models.Model):
    user = models.CharField(max_length=100)
    
    def __str__(self):
        return self.email
    
