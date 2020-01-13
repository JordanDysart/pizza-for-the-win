FROM python:3.8.0-alpine

WORKDIR /usr/src/pizza_pys

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/pizza_pys/requirements.txt
RUN pip install -r requirements.txt

# copy entrypoint.sh
COPY ./entrypoint.sh /usr/src/pizza_pys/entrypoint.sh

RUN pip install -r requirements.txt

# copy project
COPY . /usr/src/pizza_pys/

# run entrypoint.sh
ENTRYPOINT ["/usr/src/pizza_pys/entrypoint.sh"]