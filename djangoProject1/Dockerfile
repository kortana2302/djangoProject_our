FROM openjdk:20
FROM python:latest

ENV PYTHONDONTWRYTEBYTECODE 1
ENV PYTHONUNBUFERRED 1

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
RUN sed -i "s/name = 'translate'/name = 'google_translate'/g" \
    /usr/local/lib/python3.12/site-packages/google_translate/apps.py

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]