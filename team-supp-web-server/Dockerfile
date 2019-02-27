FROM tiangolo/uwsgi-nginx-flask:python3.5

LABEL maintainer="team-supp"

RUN apt-get update \
    && apt-get install -y --no-install-recommends aptitude \
    && aptitude update \
    && aptitude install -y \
    mecab \
    mecab-ipadic-utf8 \
    libmecab-dev \
    swig \
    sudo \
    && pip install --upgrade pip \
    && pip install mecab-python3 \
    && pip install opencv-python \
    && pip install pillow \
    && pip install requests \
    && rm -rf /var/lib/apt/lists/*

#    mecab-ipadic \

WORKDIR /usr/local/src
RUN git clone --depth 1 https://github.com/neologd/mecab-ipadic-neologd.git \
    && cd mecab-ipadic-neologd \
    && ./bin/install-mecab-ipadic-neologd -n -a -y \
    && echo mecab-config --dicdir"/mecab-ipadic-neologd"

# sed -e 's/sudo //g' ./libexec/install-mecab-ipadic-neologd.sh

WORKDIR /app

ENV NGINX_MAX_UPLOAD 32m

COPY ./app /app

# # Move the base entrypoint to reuse it
# RUN mv /entrypoint.sh /uwsgi-nginx-entrypoint.sh
# 
# # Copy the entrypoint that will generate Nginx additional configs
# COPY entrypoint.sh /entrypoint.sh
# RUN chmod +x /entrypoint.sh

