FROM tiangolo/uwsgi-nginx-flask:python3.5

LABEL maintainer="team-supp"

RUN apt-get update \
    && pip install --upgrade pip \
    && pip install opencv-python \
    && pip install pillow \
    && pip install requests \
    && rm -rf /var/lib/apt/lists/*

#    && apt-get install -y --no-install-recommends \

ENV NGINX_MAX_UPLOAD 32m

COPY ./app /app
