FROM python:3.10

WORKDIR /DNS_Record

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY dns_record.py .

EXPOSE 80

CMD ["python", "dns_record.py"]
