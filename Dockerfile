FROM python:latest

MAINTAINER solinj

ENV NODE_ENV=production
ENV PORT=3000

COPY      . /var/www
WORKDIR   /var/www

EXPOSE $PORT

ENTRYPOINT ["python", "wiki.py"]
