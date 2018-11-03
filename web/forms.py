import string

from django import forms

from .spotify_web_api import generate_playlist


class SearchForm(forms.Form):
    sentence = forms.CharField(label="")

    def generate_playlist(self, sentence):
        s = sentence.translate(string.punctuation)
        results = generate_playlist(s)
        return results
