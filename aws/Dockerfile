FROM python:3
RUN mkdir -p python/src
COPY test.py python/src/
COPY requirements.txt python/src/
RUN python -m pip install -r python/src/requirements.txt
WORKDIR /python/src
CMD ["python","test.py"]
