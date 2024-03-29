FROM python:3.10

ENV PYTHONUNBUFFERED=1

ARG WORKDIR=/wd
ARG USER=user
ARG UID=1000

WORKDIR ${WORKDIR}

RUN useradd --system ${USER} --uid=${UID} &&  \
    chown --recursive ${USER} ${WORKDIR}

RUN apt update && apt upgrade -y

COPY requirements.txt requirements.txt

RUN pip install --upgrade pip && \
    pip install --requirement requirements.txt

COPY --chmod=755 ./docker/app/entrypoint.sh /entrypoint.sh
COPY --chmod=755 ./docker/app/start.sh /start.sh

COPY Makefile Makefile

COPY ./manage.py manage.py
COPY ./core ./core/
COPY ./user_generator ./user_generator/

USER ${USER}

ENTRYPOINT ["/entrypoint.sh"]

VOLUME ${WORKDIR}/logs
EXPOSE 8000

