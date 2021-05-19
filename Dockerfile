FROM python:3

COPY requirements.txt /

RUN pip install -r /requirements.txt

WORKDIR /tmp

COPY main.py .

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "main:main"]
