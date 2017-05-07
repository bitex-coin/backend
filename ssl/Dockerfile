FROM alpine

RUN apk --update add bash openssl && mkdir -p /opt/bitex/ssl

WORKDIR /opt/bitex/ssl

COPY ssl/generate-server-certs /usr/local/bin/generate-server-certs

RUN chmod +x /usr/local/bin/generate-server-certs

CMD /usr/local/bin/generate-server-certs

