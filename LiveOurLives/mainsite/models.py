from django.db import models

# Create your models here.
class MinimizerRetorts(models.Model):
    shortName = models.CharField(max_length = 100)
    longName = models.CharField(max_length = 400)
    
class InfoCategories(models.Model):
    categoryName = models.CharField(max_length = 100)

class ActualInformation(models.Model):
    headline = models.CharField(max_length = 500)
    exerpt = models.CharField(max_length = 500)
    typeOfFact = models.CharField(max_length = 100) #article, study, etc
    archiveLink = models.CharField(max_length = 2000)
    liveLink = models.CharField(max_length = 2000)
    
    retorts = models.ManyToManyField(MinimizerRetorts)
    categories = models.ManyToManyField(InfoCategories)
