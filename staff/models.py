from django.db import models

# Create your models here.
class position(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title
    
class Teachers(models.Model):
    fullname = models.CharField(max_length=100)
    teach_code = models.CharField(max_length=100)
    mobile = models.CharField(max_length=100)
    position = models.ForeignKey(position,on_delete=models.CASCADE)