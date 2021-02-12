from django.db import models

# Create your models here.
class Online(models.Model):
    domain = models.CharField(max_length = 30)
    
    class Meta:
      db_table = "online"

class Dreamreal(models.Model):

    website = models.CharField(max_length = 50)
    mail = models.CharField(max_length = 50)
    name = models.CharField(max_length = 50)
    phonenumber = models.IntegerField()
    online = models.ForeignKey(Online,on_delete=models.CASCADE,null=True)

    class Meta:
        db_table = "dreamreal"

class Profile(models.Model):
   name = models.CharField(max_length = 50)
   picture = models.ImageField(upload_to = 'pictures')

   class Meta:
      db_table = "profile"