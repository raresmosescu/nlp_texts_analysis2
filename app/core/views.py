from django.shortcuts import render
from django.http import HttpResponse
from .nlp import analyze_text
from .sample_texts import samples

def home(request):
    # get form input

    # process input - codu cu analiza nlp

    return render(request, 'index.html')

def results(request):
    if request.method == 'POST':
      input_method = request.POST.get('input-method')
      print(input_method)
      # print(text, bool(text))
      print(request.POST)
      if input_method == '1':
        text = request.POST.get('text')
        if text:
          r = analyze_text(text).most_common(60)
        else:
          r = analyze_text(samples.sample1).most_common(60)
        return render(request, 'results.html', context={'results': r, 'results_str': str(dict(r))})
        
      else:
        file = str(request.FILES['file'].read())
        if file:
          r = analyze_text(file).most_common(60)
        else:
          r = analyze_text(samples.sample1).most_common(60)
        return render(request, 'results.html', context={'results': r, 'results_str': str(dict(r))})
          
    else:
      return HttpResponse('i donno man')