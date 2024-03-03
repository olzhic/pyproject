from django.db import models

# Create your models here.

class todos(models.Model):
    doing = models.CharField(max_length = 200, null=True, default = "nasrat")
    time = models.DateTimeField(blank=True,null=True, default = None)
    
    
    def __str__(self):
        return f'{self.doing}, {self.time}'
    