from datetime import timedelta

import requests
from django.db import models
from django.utils import timezone
from spotifypoetry.settings import SPOTIFY_API_URL, SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET


class SingletonModel(models.Model):

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        self.pk = 1
        super(SingletonModel, self).save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        pass

    @classmethod
    def load(cls):
        obj, created = cls.objects.get_or_create(pk=1)
        return obj


class Track(models.Model):
    title = models.CharField(max_length=256)
    external_url = models.URLField()


class Token(SingletonModel):
    expiry_datetime = models.DateTimeField(default=timezone.now())
    token_string = models.CharField(max_length=128, unique=True)
    @property
    def token(self):
        now = timezone.now()
        time_since_expiry = now - self.expiry_datetime
        if time_since_expiry > timedelta(seconds=600):
            self.token_string = self._request_token()
            print("Got new token string: {}".format(self.token_string))
            return self.token_string

    @staticmethod
    def _request_token():
        """
        Request a token from Spotify.
        """

        headers = {'Accept': 'application/json'}
        data = [('grant_type', 'client_credentials')]
        response = requests.post(SPOTIFY_API_URL,
                                 headers=headers,
                                 data=data,
                                 auth=(SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET))
        try:
            return response.json()['access_token']

        except (KeyError, TypeError):
            raise