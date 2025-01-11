from django.views.generic import TemplateView
from django.shortcuts import render


# Create your views here.
def func_templates(request):
    return render(request, 'second_task/func_template.html')
      

class ClassTemplates(TemplateView):
    template_name = 'second_task/class_template.html'
    
