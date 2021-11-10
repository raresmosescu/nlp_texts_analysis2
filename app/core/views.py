from django.shortcuts import render
from django.http import HttpResponse
from .nlp import analyze_text
from .sample_texts import samples

def home(request):
    # get form input

    # process input - codu cu analiza nlp

    return render(request, 'index.html')

def results(request):
    text = request.POST.get('text')
    print(text, bool(text))
    if text:
        r = analyze_text(text).most_common(60)
    else:
        r = analyze_text(samples.sample1).most_common(60)
    return render(request, 'results.html', context={'results': r, 'results_str': str(dict(r))})