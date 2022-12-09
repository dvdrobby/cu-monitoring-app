from django.shortcuts import render
from django.views.generic import CreateView, ListView
from django.urls import reverse

# from .models import FormModel
from .forms import FormForm
from .models import FormModel

def titleView(request, slug):
    context = {
        'slug': slug
    }
    return render(request, 'apps/index.html', context)

# class FormView(CreateView):
#     model = FormModel
#     # template_name: 'apps/create_form.html'
#     fields = '__all__'
#     template_name: 'apps/create_form.html'


#     def get_success_url(self) -> str:
#         return reverse('index')

class ListForm(ListView):
    model= FormModel
    template_name= 'apps/index.html'

  

