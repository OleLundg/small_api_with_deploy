FROM python:latest

WORKDIR /src

COPY ./src /src

RUN pip install --no-cache-dir --upgrade pip && pip install --no-cache-dir -r requirements.txt

CMD ["python", "./src/web.py"]
