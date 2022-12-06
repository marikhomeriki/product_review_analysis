FROM python:3.9
EXPOSE 8080

WORKDIR /app
COPY . ./

RUN pip install --no-cache-dir -r requirements.txt

CMD exec uvicorn api:app --host 0.0.0.0 --port 8080
