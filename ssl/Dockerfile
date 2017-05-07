FROM alpine

RUN apk --update add bash openssl

WORKDIR /opt/bitex/ssl

COPY ssl/generate-server-certs /usr/local/bin/generate-server-certs

RUN chmod +x /usr/local/bin/generate-server-certs

CMD /usr/local/bin/generate-server-certs

