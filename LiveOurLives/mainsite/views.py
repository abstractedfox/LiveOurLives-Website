from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import MinimizerRetorts


# Create your views here.
def index(request):
    retortsQueryOutput = MinimizerRetorts.objects.all();
    context = {"MinimizerRetorts": retortsQueryOutput,
    "defaultRetort": retortsQueryOutput.first()
    }
    
    if request.method == "POST":
        print("we post")
        if request.POST.get("minimizer-dropdown"):
            print(request.POST.get("minimizer-dropdown"))
            #note to me: yes this is actually supposed to be a single =
            context["defaultRetort"] = retortsQueryOutput.filter(shortName__exact = request.POST.get("minimizer-dropdown")).first()
    
    return render(request, 'mainsite/index.html', context)
