# spotifypoetry

## Description
Django project to create spotify poems.

Takes a sentence as input, and outputs a list of spotify URLs.
The songs in sequence spell out the original sentence.

Interfaces:
- HTML form input (`http://localhost:8000`)
- API (GET request with query string)

## Docker
I've built a docker image, which can be run on your local machine.
`jaronrademeyer/spotifypoetry`

The docker container requires 4 parameters at runtime:
1) Map local port 8000 to container port 8000
2) Spotify Client ID
3) Spotify Secret ID
4) Run in interactive mode

The following is an example:
`docker run -it -p 8000:8000 -e CLIENT_ID='MY_CLIENT_ID_HERE' -e SECRET='MY_SECRET_HERE' jaronrademeyer/spotifypoetry`

You should see output like the following:

```
Performing system checks...

System check identified no issues (0 silenced).
November 05, 2018 - 18:51:41
Django version 2.1.2, using settings 'spotifypoetry.settings'
Starting development server at http://0.0.0.0:8000/
Quit the server with CONTROL-C.

```

## Local build and installation
Use the Docker container instead if you're just testing it out.

- clone repo
- set up virtualenv in python 3.5+ 
- `pip install -r requirements.txt`
- Edit settings.py and insert your spotify `CLIENT ID` and `SECRET`
- `python manage.py migrate`
- `python manage.py runserver`

## API
### Example:
http://localhost:8000/api/?sentence=write%20me%20a%20poem

### Endpoint: 
- http://localhost:8000/api/
### QueryString: 
- sentence (string)
### Output:
JSON dict in the following structure:

`{"results": ["https://open.spotify.com/track/1FEyOlk0IHBI3U1wMRnJyQ"]}`


