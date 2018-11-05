FROM python:3.6

RUN mkdir /app
WORKDIR /app
COPY . /app
RUN pip install -r ./requirements.txt

EXPOSE 8000
STOPSIGNAL SIGINT
ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:8000"]