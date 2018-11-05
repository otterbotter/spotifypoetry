import json
import string

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView, FormView

from web.forms import SearchForm
from web.spotify_web_api import generate_playlist


class SearchView(FormView):
    template_name = "web/search.html"
    form_class = SearchForm
    success_url = '/'

    def form_valid(self, form):
        super(SearchView, self).form_valid(form)
        playlist = form.generate_playlist(form.cleaned_data.get('sentence', ''))
        html = "<html>"
        for url in playlist:
            html += "<p><a href="+url+">"+url+"</a></p>"
        html += "</html>"
        return HttpResponse(html)


def search_api(request):
    sentence = request.GET.get('sentence', None)
    if sentence:
        result_dict = {}
        s = sentence.translate(string.punctuation)
        results = generate_playlist(s)
        result_dict['results'] = results
        return HttpResponse(json.dumps(result_dict))