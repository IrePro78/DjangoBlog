FROM python:3.9
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt


COPY entrypoint.sh entrypoint.sh
RUN sed -i 's/\r$//g' /app/entrypoint.sh
RUN chmod +x /app/entrypoint.sh

COPY . .

# run entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]

