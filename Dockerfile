FROM python:3.10-slim

WORKDIR /claim_app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY claims.py .

EXPOSE 80

CMD ["python", "claims.py"]
