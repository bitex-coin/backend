FROM alpine
MAINTAINER Clebson Derivan <cderivan@gmail.com>

ARG USER_ID
ARG GROUP_ID

ENV HOME /bitex

# add user with specified (or default) user/group ids
ENV USER_ID ${USER_ID:-5000}
ENV GROUP_ID ${GROUP_ID:-5000}

# add our user and group first to make sure their IDs get assigned consistently, regardless of whatever dependencies get added
RUN adduser -D -u ${USER_ID} -g ${GROUP_ID} -h /bitex bitex

# grab gosu for easy step-down from root
ENV GOSU_VERSION 1.7
RUN set -x \
        && apk add --update curl gnupg \
        && curl -sSL "https://github.com/tianon/gosu/releases/download/1.7/gosu-amd64" > /usr/local/bin/gosu \
        && curl -sSL "https://github.com/tianon/gosu/releases/download/1.7/gosu-amd64.asc" > /usr/local/bin/gosu.asc \
        && export GNUPGHOME="$(mktemp -d)" \
        && gpg --keyserver ha.pool.sks-keyservers.net --recv-keys B42F6819007F00F88E364FD4036A9C25BF357DD4 \
        && gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \
        && rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \
        && chmod +x /usr/local/bin/gosu \
        && gosu nobody true \
        && apk del --purge curl gnupg \
        && rm -rf /root/.gnupg \
	&& rm -rf /var/cache/apk/* 

RUN apk --update add bash git build-base ruby ruby-dev libffi-dev 

RUN git clone --depth 1 https://github.com/bitex-coin/frontend.git
COPY frontend/_config.yml frontend

RUN echo 'gem: --no-document' > /etc/gemrc && gem install jekyll json jekyll-paginate jekyll-multiple-languages-plugin

ADD ./frontend/bin /usr/local/bin

COPY ./frontend/docker-entrypoint.sh /usr/local/bin/
ENTRYPOINT ["docker-entrypoint.sh"]

CMD ["jekyll_server"]


