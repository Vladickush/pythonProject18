from django.views.generic import TemplateView
from django.shortcuts import render


# Create your views here.
def func_templates(request):
    return render(request, 'func_template.html')
    #return render(request, 'second_task/func_template.html')

class ClassTemplates(TemplateView):
    template_name = 'class_template.html'
    #template_name = 'second_task/class_template.html'
