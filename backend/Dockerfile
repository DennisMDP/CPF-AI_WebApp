# Verwendung eines Basis-Images
FROM python:3.11

# Definition Arbeitsverzeichnis
WORKDIR /app

# Installieren der Abhängigkeiten
COPY ./requirements.txt /app
RUN pip install --no-cache-dir -r requirements.txt

# Kopieren des Codes
COPY . /app

# Verfügbarkeit des Ports
EXPOSE 8000

# Start Applikation
#CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0"]
CMD ["uvicorn", "main:app", "--host", "0.0.0.0"]
