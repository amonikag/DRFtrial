from django.db import models
import datetime
import os

def filepath(request,filename):
    old_filename=filename
    timern      =datetime.datetime.now().strftime('%Y%m%d%H%M%S')
    filename    =old_filename.split(".")[0]+timern+"."+old_filename.split(".")[1]
    return os.path.join('uploads/',filename)

# Create your models here.
class Music(models.Model):
    name        =models.CharField(max_length=250,null=False,default="NULL")
    album       =models.CharField(max_length=500,default="Null")
    singer      =models.CharField(max_length=250,default="Null")
    cover        =models.ImageField(upload_to=filepath,null=True,blank=True)

