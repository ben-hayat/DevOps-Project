# official Python runtime as parent image 
FROM python:3.7-slim

COPY requirements.txt /tmp/
RUN pip install -r /tmp/requirements.txt

RUN useradd --create-home appuser
WORKDIR /home/appuser
USER appuser

COPY MainScores.py .
COPY utils.py .
COPY Scores.txt .
COPY templates/* templates/
EXPOSE 5000/tcp

CMD [ "python", "MainScores.py" ]
