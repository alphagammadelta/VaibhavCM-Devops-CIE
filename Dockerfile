FROM python:3
RUN pip install flask
COPY app.py .
cmd ["python3", "app.py"]
