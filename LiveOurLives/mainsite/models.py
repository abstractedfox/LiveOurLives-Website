from django.db import models

# Create your models here.
class MinimizerRetorts(models.Model):
    shortName = models.CharField(max_length = 100)
    longName = models.CharField(max_length = 400, blank = True)
    display = models.BooleanField(default = True)

    def __str__(self):
        return self.shortName
    
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

    def __str__(self):
        return self.categoryName

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
    PAPER = "PAPER"
    types = [
        (ARTICLE_STUDY, "Article on a study"),
        (ARTICLE_OP, "Opinion piece"),
        (ARTICLE_STATS, "Article on statistics"),
        (ANECDOTE, "Personal anecdote"),
        (STUDY, "Study"),
        (STATS, "Statistics & Models"),
        (EXAMPLE, "Example"),
        (OTHER_MIXED, "Other / Mixed"),
        (PAPER, "Paper")
    ]

    #Type of source:
    INDIVIDUAL_ACCOUNT = "INDIVIDUAL ACCOUNT"
    MEDICAL_PRO = "MEDICAL PROFESSIONAL"
    PRO_GROUP = "GROUP OF PROFESSIONALS"
    ENG = "ENGINEER"
    GOV_BODY = "GOVERNING BODY"
    JOURNALIST = "JOURNALIST"
    ECONOMIST = "ECONOMIST"
    OTHER_PRO = "OTHER PROFESSIONAL"
    sources = [
        (INDIVIDUAL_ACCOUNT, "Individual account"),
        (MEDICAL_PRO, "Medical professional"),
        (PRO_GROUP, "Group of professionals"),
        (ENG, "Engineer"),
        (GOV_BODY, "Governing body"),
        (JOURNALIST, "Journalist"),
        (OTHER_MIXED, "Other / Mixed"),
        (OTHER_PRO, "Other / Professional"),
        (ECONOMIST, "Economist")
    ]

    type = models.CharField(max_length = 150, choices = types, default = OTHER_MIXED)
    source = models.CharField(max_length = 150, choices = sources, default = OTHER_MIXED)
    
    archiveLink = models.CharField(max_length = 2000, blank = True, default = "")
    liveLink = models.CharField(max_length = 2000, blank = True, default = "")

    headline = models.CharField(max_length = 500)
    publication = models.CharField(max_length = 150, blank = True, default="")
    exerpt = models.CharField(max_length = 600, blank = True, default = "")
    author = models.CharField(max_length = 1000, blank = True, default = "")
    authors_title = models.CharField(max_length = 150, blank = True, default = "") #title, credential, or other of the author
    participants = models.IntegerField(blank = True, default = 0) #Participants in a study etc
    meta_info = models.CharField(max_length = 1000, blank = True, default = "") #Any extra info we'd like to include

    datePublished = models.DateField(null = True, blank = True)
    dateArchived = models.DateField(null = True, blank = True)
    
    retorts = models.ManyToManyField(MinimizerRetorts)
    categories = models.ManyToManyField(InfoCategories)

    display = models.BooleanField(default = True)
    
    #Assign which part of the entry should be emphasized in the UI
    emphasisChoices = [
        ("HEADLINE", "HEADLINE"),
        ("EXCERPT", "EXCERPT")
    ]
    emphasis = models.CharField(max_length = 100, default = emphasisChoices[0], choices = emphasisChoices)

    def __str__(self):
        return self.headline + " " + self.liveLink
        
class MultiExcerpt(models.Model):
    #Table for assigning multiple excerpts to a single entry
    excerpt = models.CharField(max_length = 500)
    parentEntry = models.ForeignKey(ActualInformation, on_delete=models.CASCADE)
    
    def __str__(self):
        return excerpt

class ImageInfo(models.Model):
    localPath = models.CharField(max_length = 200, blank = True, default = "#")
    altText = models.CharField(max_length = 200, blank = True, default = "")
    
    author = models.CharField(max_length = 200, blank = True, default = "")
    sourcedFrom = models.CharField(max_length = 500, blank = True, default = "")
    sourceLink = models.CharField(max_length = 500, blank = True, default = "")
    dateGathered = models.DateField(null = True, blank = True)
    
    licenseInfo = models.CharField(max_length = 2000, blank = True, default = "")
    changesMade = models.CharField(max_length = 1000, blank = True, default = "") #Some licenses require publishing whether changes were made to an image

    def __str__(self):
        return self.altText;
