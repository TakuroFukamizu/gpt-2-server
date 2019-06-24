FROM gpt-2

COPY ./src/generate.py /gpt-2/src/
COPY ./src/app.py /gpt-2/src/

COPY requirements.txt ./
RUN set -x; \
    pip --no-cache-dir install -r requirements.txt

WORKDIR /gpt-2
CMD [ "sh", "-c", \
    "python3 src/app.py" \
    ]