FROM python:3.8.2-alpine

WORKDIR /current

RUN apk --update --upgrade add --no-cache gcc musl-dev jpeg-dev zlib-dev libffi-dev cairo-dev pango-dev gdk-pixbuf-dev vim && apk add libpq && apk add postgresql-dev

RUN python3 -m pip install --upgrade pip

RUN pip3 install setuptools==45

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt && pip install psycopg2

EXPOSE 3002

COPY . .

CMD [ "python", "server.py","runserver" ]
