# ----- BASE IMAGE -----
# FROM python:3
# ----- BASE IMAGE -----
FROM artifactory.turkcell.com.tr/local-docker-dist-dev/com/turkcell/object-storage/python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD [ "uvicorn", "main:app","--host","0.0.0.0" ]