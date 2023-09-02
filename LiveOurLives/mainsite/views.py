from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import MinimizerRetorts


# Create your views here.
def index(request):
    retortsQueryOutput = MinimizerRetorts.objects.all();
    context = {"MinimizerRetorts": retortsQueryOutput,
    "defaultRetort": retortsQueryOutput.last()
}
    print(context["defaultRetort"])
    
    return render(request, 'mainsite/index.html', context)
