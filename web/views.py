from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, FormView

from web.forms import SearchForm


class SearchView(FormView):
    template_name = "web/search.html"
    form_class = SearchForm
    success_url = '/'

    def form_valid(self, form):
        super(SearchView, self).form_valid(form)
        playlist = form.generate_playlist(form.cleaned_data.get('sentence', ''))
        return HttpResponse("<html>{}</html>".format(playlist))

