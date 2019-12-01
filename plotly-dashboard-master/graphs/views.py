from django.http import HttpResponse
from django.views.generic import TemplateView
from . import plots, models

from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic

class SimpleCandlestickWithPandas(TemplateView):
    template_name = 'summary.html'
    def get_context_data(self, **kwargs):
        context = super(SimpleCandlestickWithPandas, self).get_context_data(**kwargs)
        context['model'] = models.get_summary()
        context['plot'] = models.plot1()
        # context['piechart'] = plots.pie_chart()
        return context
# class SignUp(generic.CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'signup.html'
