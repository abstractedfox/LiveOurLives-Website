from django.db import models

# Create your models here.
class MinimizerRetorts(models.Model):
    shortName = models.CharField(max_length = 100)
    longName = models.CharField(max_length = 400)
    display = models.BooleanField(default = False)
    
class InfoCategories(models.Model):
    #Available categories
    LC_EFFECTS = "LONG COVID EFFECTS ON BODY"
    LC_ANECDOTES = "LONG COVID ANECDOTES"
    LC = "LONG COVID"
    MITIGATION_AND_EFFICACY = "MITIGATION AND EFFICACY"
    IMMUNE_SYSTEM = "IMMUNE SYSTEM"
    ARTICLE = "ARTICLE"
    STUDY = "STUDY"
    ECONOMY = "ECONOMY"
    TRANSMISSIBILITY = "TRANSMISSIBILITY"
    VACCINES = "VACCINES"
    MISC = "Misc."
    categories = [
        (LC_EFFECTS, "Long covid & effects on the body"),
        (LC_ANECDOTES, "Long covid anecdotes"),
        (LC, "Long covid"),
        (MITIGATION_AND_EFFICACY, "Mitigation and efficacy"),
        (IMMUNE_SYSTEM, "Immune system"),
        (ARTICLE, "Article"),
        (STUDY, "Study"),
        (ECONOMY, "Economy"),
        (TRANSMISSIBILITY, "Transmission"),
        (VACCINES, "Vaccines"),
        (MISC, "Misc")
    ]

    categoryName = models.CharField(max_length = 100, choices = categories, default = MISC)

class ActualInformation(models.Model):
    OTHER_MIXED = "OTHER/MIXED"

    #Type of piece:
    ARTICLE_STUDY = "ARTICLE STUDY"
    ARTICLE_OP = "ARTICLE OPINION"
    ARTICLE_STATS = "ARTICLE STATISTICS"
    ANECDOTE = "ANECDOTE"
    STUDY = "STUDY"
    STATS = "STATISTICS"
    EXAMPLE = "EXAMPLE"
    types = [
        (ARTICLE_STUDY, "Article on a study"),
        (ARTICLE_OP, "Opinion piece"),
        (ARTICLE_STATS, "Article on statistics"),
        (ANECDOTE, "Personal anecdote"),
        (STUDY, "Study"),
        (STATS, "Statistics & Models"),
        (EXAMPLE, "Example"),
        (OTHER_MIXED, "Other / Mixed")
    ]

    #Type of source:
    INDIVIDUAL_ACCOUNT = "INDIVIDUAL ACCOUNT"
    MEDICAL_PRO = "MEDICAL PROFESSIONAL"
    PRO_GROUP = "GROUP OF PROFESSIONALS"
    ENG = "ENGINEER"
    GOV_BODY = "GOVERNING BODY"
    sources = [
        (INDIVIDUAL_ACCOUNT, "Individual account"),
        (MEDICAL_PRO, "Medical professional"),
        (PRO_GROUP, "Group of professionals"),
        (ENG, "Engineer"),
        (GOV_BODY, "Governing body"),
        (OTHER_MIXED, "Other / Mixed")
    ]

    type = models.CharField(max_length = 150, choices = types, default = OTHER_MIXED)
    source = models.CharField(max_length = 150, choices = sources, default = OTHER_MIXED)

    headline = models.CharField(max_length = 500)
    exerpt = models.CharField(max_length = 500)
    typeOfFact = models.CharField(max_length = 100) 
    archiveLink = models.CharField(max_length = 2000)
    liveLink = models.CharField(max_length = 2000)

    participants = models.IntegerField(null = True) #Participants in a study etc

    datePublished = models.DateField(null = True)
    dateArchived = models.DateField(null = True)
    
    retorts = models.ManyToManyField(MinimizerRetorts)
    categories = models.ManyToManyField(InfoCategories)

    display = models.BooleanField(default = False)