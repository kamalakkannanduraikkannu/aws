FROM python:3-alpine

WORKDIR /usr/src/app

COPY requirements.txt ./
COPY app.py ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0" ]