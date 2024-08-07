from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from django.core.validators import MaxValueValidator

# Create your models here.

class Profile(models.Model):
    profile=CloudinaryField('profile')
    bio=models.CharField(max_length=60)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    phone=models.IntegerField()
    class Meta:
        ordering=['-profile']

class Projects(models.Model):
    name=models.CharField(max_length=30)
    image=CloudinaryField('project')
    design=models.IntegerField(default=0)
    usability=models.IntegerField(default=0)
    content=models.IntegerField(default=0)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    description=models.TextField(max_length=320)
    link=models.URLField(max_length=60)
    date=models.DateField(auto_now=True)
    screen1=CloudinaryField('screenshot1')
    screen2=CloudinaryField('screenshot2')

    class Meta:
        ordering=['-name']

    def __str__(self):
        self.name
    @classmethod
    def search_project(cls,word):
        searched=cls.objects.filter(name__icontains=word)
        return searched


class Comments(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    comment=models.TextField(max_length=200)
    pro_id=models.IntegerField(default=0)




class Rates(models.Model):
    design=models.PositiveIntegerField(default=0,validators=[MaxValueValidator(10)])
    usability=models.PositiveIntegerField(default=0,validators=[MaxValueValidator(10)])
    content=models.PositiveIntegerField(default=0,validators=[MaxValueValidator(10)])
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    project=models.IntegerField(default=0)

