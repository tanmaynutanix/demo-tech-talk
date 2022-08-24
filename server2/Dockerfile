FROM python:3.8

# This is required for cryptography python package.
RUN apt-get update && apt-get install -y gcc g++ make

ENV PYTHONUNBUFFERED 1

RUN python -m pip install --upgrade pip
RUN apt-get install vim -y

COPY . /app
WORKDIR /app

RUN pip install -r requirements_app2.txt

ENTRYPOINT ["python"]
CMD ["main2.py"]

