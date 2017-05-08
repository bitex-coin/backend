FROM alpine

RUN apk --update add bash git build-base ruby ruby-dev libffi-dev 
RUN git clone --depth 1 https://github.com/bitex-coin/frontend.git
RUN echo 'gem: --no-document' > /etc/gemrc && gem install jekyll json jekyll-paginate jekyll-multiple-languages-plugin

COPY frontend/entrypoint /usr/local/bin/entrypoint
RUN chmod +x /usr/local/bin/entrypoint

CMD /usr/local/bin/entrypoint

