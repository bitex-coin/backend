FROM python:3
ADD  requirements.txt /tmp/requirements.txt
RUN pip install -r /tmp/requirements.txt
ADD receiver /code
ADD receiver/api_receive.ini /code
ADD libraries /libraries
WORKDIR /code
ENTRYPOINT ["python"]
CMD [ "main.py", "-c", "api_receive.ini"]

