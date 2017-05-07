FROM python:2.7
ADD  requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
ADD match /code
ADD bitex.ini /code
ADD libraries /libraries
WORKDIR /code
ENTRYPOINT ["python"]
CMD [ "main.py", "-i", "trade_demo" ]
