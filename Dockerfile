FROM python:3.6-alpine
LABEL author=hieu

COPY requirements.txt /tmp/
RUN pip3 install -r /tmp/requirements.txt \
    && rm -rf ~/.cache/pip

COPY domain /app/domain/
COPY entrypoint.sh /app/

WORKDIR /app/
ENV PYTHONPATH "${PYTHONPATH}:${PWD}"
RUN chmod u+x entrypoint.sh

ENTRYPOINT ["./entrypoint.sh"]