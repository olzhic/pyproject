from django.db import models

# Create your models here.

class todos(models.Model):
    doing = models.CharField(max_length = 200)
    time = models.DateTimeField()
    
    
    def __str__(self):
        return f'{self.doing}, {self.time}'
    