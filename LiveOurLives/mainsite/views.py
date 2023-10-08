from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render, redirect
from .models import MinimizerRetorts, InfoCategories, ActualInformation, ImageInfo
import random

# Create your views here.  

#Note: No urls should go here directly, this is so we can use the same code for index() and indexSelection() without having to get weird handling GET/POST stuff
def renderPage(request, chosenRetort):
    retortsQueryOutput = MinimizerRetorts.objects.filter(display__exact = True).exclude(shortName__exact = "BLANK")
    blankOption = MinimizerRetorts.objects.filter(shortName__exact = "BLANK")

    context = {"MinimizerRetorts": retortsQueryOutput,
    "defaultRetort": retortsQueryOutput.first(),
    "retortResults": {},
    "infoTypes": ActualInformation.types,
    "infoSources": ActualInformation.sources,
    "minimizerImage": "mainsite/minimizers/wen.png",
    "blankOption": blankOption,
    "extraInfo": {}
    }
    
    #Get an image to display next to the dropdown
    minimizers = list(ImageInfo.objects.all())
    context["minimizerImage"] = random.sample(minimizers, 1)[0]
        
    
    filteredResults = retortsQueryOutput.filter(shortName__exact = chosenRetort).first()
    if chosenRetort != "" and filteredResults != None:
        context["defaultRetort"] = filteredResults
        context["retortResults"] = ActualInformation.objects.filter(retorts__exact = filteredResults, display__exact = True)
    else:
        if blankOption.first() != None:
            context["defaultRetort"] = blankOption.first()

    return render(request, 'mainsite/index.html', context)

def index(request):
    if request.method == "POST":
        if request.POST.get("minimizer-dropdown"):
            #return renderPage(request, request.POST.get("minimizer-dropdown"))
            url = "/" + request.POST.get("minimizer-dropdown")
            return redirect(url)

    return renderPage(request, "")

def indexSelection(request, selection):
    return renderPage(request, selection)
