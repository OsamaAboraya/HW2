FROM python:3.8.5
COPY requirements.txt ./
RUN pip install -r requirements.txt
COPY hw2.py .
EXPOSE 5000
CMD python hw2.py
