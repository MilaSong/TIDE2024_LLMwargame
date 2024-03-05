FROM python:3.12

RUN apt update && apt install -y gdal-bin libgdal-dev
COPY requirements.txt requirements.txt
RUN apt update && apt install -y gdal-bin libgdal-dev
RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r requirements.txt

RUN mkdir -p /uploads

EXPOSE 8080
