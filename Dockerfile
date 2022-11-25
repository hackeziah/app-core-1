# FROM python:3.9.6-slim-buster
# ENV PYTHONUNBUFFERED 1

# WORKDIR /app

# # set environment variables
# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

# # install dependencies
# RUN pip install --upgrade pip
# COPY ./requirements.txt .
# RUN pip install -r requirements.txt

# COPY . .

# CMD [ "uvicorn", "app.main.app", "--host", "0.0.0.0", "--port", "8000"]
# # EXPOSE 8000

FROM python:3.9
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY ./requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /app
EXPOSE 8000

# syntax=docker/dockerfile:1

# FROM python:3.8-slim-buster

# ENV PYTHONDONTWRITEBYTECODE 1
# ENV PYTHONUNBUFFERED 1

# WORKDIR /app

# RUN pip install --upgrade pip
# COPY requirements.txt requirements.txt
# RUN pip install -r requirements.txt

# RUN pip install --upgrade pip
# COPY ./requirements.txt .
# RUN pip install -r requirements.txt
# COPY . .
# CMD [ "uvicorn", "app.main.app", "--host", "0.0.0.0", "--port", "8000"]