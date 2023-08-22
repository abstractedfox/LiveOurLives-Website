from django.db import models

# Create your models here.
class Retorts(models.Model):
    shortName = models.CharField(max_length = 100)
    longName = models.CharField(max_length = 400)

class Facts(models.Model):
    headline = models.CharField(max_length = 500)
    exerpt = models.CharField(max_length = 500)
    typeOfFact = models.CharField(max_length = 100) #article, study, etc
    archiveLink = models.CharField(max_length = 2000)
    liveLink = models.CharField(max_length = 2000)
    
class Categories(models.Model):
    categoryName = models.CharField(max_length = 100)
    retorts = models.ManyToManyField(Retorts)
    facts = models.ManyToManyField(Facts)
