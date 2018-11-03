# spotifypoetry

## Description
Takes a sentence as input, and outputs a list of spotify URLs.
The songs in sequence spell out the original sentence.

Interfaces:
- HTML form input (`http://localhost:8000`)
- API (get request with query string)

## Install
- clone repo
- set up virtualenv in python 3.5+ 
- `pip install -r requirements.txt`
- Edit settings.py and insert your spotify `CLIENT ID` and `SECRET`
- `python manage.py migrate`
- `python manage.py runserver`

## API
###Endpoint: 
- http://localhost:8000/api/
### QueryString: 
- sentence (string)
### Output:
JSON dict in the following structure:

`{"results": ["https://open.spotify.com/track/7JeKXMQKm6GoLGTkNy2jZ0", "https://open.spotify.com/track/13HVjjWUZFaWilh2QUJKsP", "https://open.spotify.com/track/6Qhg7DZ4JxL0i5lY0B8A69"]}`

