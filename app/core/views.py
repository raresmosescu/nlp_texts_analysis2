from django.shortcuts import render
from django.http import HttpResponse
from .nlp import analyze_text

def home(request):
    # get form input

    # process input - codu cu analiza nlp

    return render(request, 'index.html')

def results(request):
    text = request.POST.get('text')
    print(analyze_text(text))
    return HttpResponse(str(dict(analyze_text(text))))