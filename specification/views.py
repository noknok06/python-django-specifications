# specification/views.py

from django.shortcuts import render

# specification/views.py

from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic import ListView

from .models import StandardChangeMst
from .forms import StandardChangeMstForm


def specification_home(request):
    return render(request, 'specification/specification_home.html')

class StandardChangeMstCreateView(CreateView):
    model = StandardChangeMst
    form_class = StandardChangeMstForm
    template_name = 'specification/standardchange_form.html'
    success_url = reverse_lazy('standardchange_list')  # 適切な成功URLに変更してください

class StandardChangeMstListView(ListView):
    model = StandardChangeMst
    template_name = 'specification/standardchange_list.html'
    context_object_name = 'standard_changes'
