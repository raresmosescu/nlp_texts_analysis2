from django.shortcuts import render
from django.http import HttpResponse
from core.generate_image import generate_by_dict

from core.models import Feedbacks
from .nlp import analyze_text, analyze_whatsapp_export
from .sample_texts import samples
from .models import Noun


def home(request):
  if request.method == 'POST':
    feedback = request.POST.get('feedback')
    if feedback:
      Feedbacks.objects.create(feedback=feedback)
  return render(request, 'index_EN.html')

def results(request):
    if request.method == 'POST':
      input_method = request.POST.get('input-method')
      print(input_method)
      print(request.POST)
      if input_method == '1':
        text = request.POST.get('text')
        if text:
          r = analyze_text(text).most_common(60)
        else:
          r = analyze_text(samples.sample1).most_common(60)
        generate_by_dict(dict(r))
        return render(request, 'results_EN.html', context={'results': r, 'results_str': str(dict(r))})
        
      else:
        text = request.FILES['file'].read()
        if text:
          r = analyze_whatsapp_export(text).most_common(60)
          entry_list = []
          for n in r:
            entry_list.append(Noun(result_id=-1, word=n[0], freq=n[1], score=-1))
          Noun.objects.bulk_create(entry_list)
        else:
          r = analyze_whatsapp_export(samples.sample1).most_common(60)
        generate_by_dict(dict(r))
        return render(request, 'results_EN.html', context={'results': r, 'results_str': str(dict(r))})
          
    else:
      return HttpResponse('i donno man')
      # aah don't worry man, life is good, drink a beer or somethin

def print_db(request):
    html = '<div><ul>'
    for obj in Noun.objects.all():
        html += f'<li>{obj.word}, {obj.freq}</li>'
    html += '</ul></div>'
    return HttpResponse(html)
