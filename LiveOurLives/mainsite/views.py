from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import MinimizerRetorts, InfoCategories, ActualInformation


# Create your views here.
def index(request):
    retortsQueryOutput = MinimizerRetorts.objects.all();

    context = {"MinimizerRetorts": retortsQueryOutput,
    "defaultRetort": retortsQueryOutput.first(),
    "retortResults": {},
    "infoTypes": ActualInformation.types,
    "infoSources": ActualInformation.sources
    }
    
    if request.method == "POST":
        if request.POST.get("minimizer-dropdown"):
            chosenRetort = retortsQueryOutput.filter(shortName__exact = request.POST.get("minimizer-dropdown")).first()
            
            #note to me: yes this is actually supposed to be a single =
            context["defaultRetort"] = chosenRetort
            
            context["retortResults"] = ActualInformation.objects.filter(retorts__exact = chosenRetort)
    
    else:
        blankOption = retortsQueryOutput.filter(shortName__exact = "BLANK")
        if blankOption.count() == 1:
            context["defaultRetort"] = blankOption.first()


    return render(request, 'mainsite/index.html', context)
