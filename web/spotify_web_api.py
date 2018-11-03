from itertools import combinations
from web.models import Track, Token
import requests
import logging

logger = logging.getLogger(__name__)


def _http_request(url, method="get", headers=None, params=None, data=None, auth=None):
    """
    Make an HTTP request and return the response.
    """
    try:
        method = requests.post if method == "post" else requests.get
        response = method(url, headers=headers, params=params, data=data, auth=auth)
        response_json = response.json()
        logger.debug("Response:")
        logger.debug("      -- " + response)
        if response.status_code != 200:
            raise Exception(response.text)
    except ValueError:
        return response.text
    except Exception:
        raise
    return response_json


def _split_sentence(l, splits):
    """
    Splits the sentence into substrings
    Credit: Asirhc
    """
    output = []
    for i, index in enumerate(splits):
        if i != len(splits) - 1:
            next_spot = splits[i + 1]
            output += [l[index:next_spot]]
        else:
            output += [l[index:]]
    print(output)
    return output


def generate_playlist(sentence):
    """
    Returns a list of urls, in correct order.
    :return: list
    """
    token = Token.load().token
    words_split = sentence.split(' ')
    for i in range(0, len(words_split)):
        selected_range = range(1, len(words_split))
        combs = combinations(selected_range, i)
        for c in combs:
            indexes = [0, ] + list(c)
            playlist = [' '.join(x) for x in _split_sentence(words_split, indexes)]
            urls = _get_playlist_urls(playlist, token=token)
            print(urls)
            if None not in urls:
                return urls
    return ['No matches found, sorry.']


def _get_playlist_urls(list_of_titles, token=None):
    if not token:
        raise Exception("No token provided.")
    urls = [_get_url_if_track_exists(t, token) for t in list_of_titles]
    return urls


def _get_url_if_track_exists(track_title, token=None):
    """
    Gets a url for a given track title, after checking for previous matches stored locally.
    :param track_title: string
    :return: url string
    """
    if not token:
        raise Exception("No token provided.")
    track_objects = Track.objects.filter(title=track_title)
    if track_objects:
        track_object = track_objects[0]
        return track_object.external_url
    url = "https://api.spotify.com/v1/search?q=\"{}\"&type=track".format(track_title)
    tracks = requests.get(url,
                          headers={'Authorization': 'Bearer {}'.format(token)})
    if tracks:
        for track in tracks.json()['tracks']['items']:
            track_name = track['name'].lower()
            if track_name == track_title.lower():
                track_object = Track.objects.create(title=track_title, external_url=track['external_urls']['spotify'])
                return track_object.external_url
    else:
        return None
