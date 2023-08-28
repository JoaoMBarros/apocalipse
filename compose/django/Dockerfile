FROM python:3.10.0

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ARG PROJECT_DIR=/apocalipse

RUN mkdir -p ${PROJECT_DIR}
COPY ./apocalipse_api ${PROJECT_DIR}

WORKDIR ${PROJECT_DIR}

RUN python -m pip install -r requirements.txt
RUN python manage.py makemigrations sobreviventes

COPY ./compose/django/entry.sh /entry.sh
RUN chmod +x /entry.sh
ENTRYPOINT ["/entry.sh"]
