# FROM python:3.7
FROM python:3.7-alpine

RUN apt-get update
RUN apt-get install -y libsm6 libxext6 libxrender-dev
RUN apt-get install -y libgl1-mesa-glx

COPY . /app
WORKDIR /app

COPY requirements.txt /
RUN pip install -r /requirements.txt

# RUN pip install -r requirements.txt

# ENTRYPOINT ["python"]
# CMD ["app.py"]

EXPOSE 80

#CMD ["gunicorn", "--bind 0.0.0.0:80", "app:app"]

CMD ["gunicorn", "-b", "0.0.0.0:80", "app:app"]

# This will work in the port 8000
# CMD ["gunicorn", "-w 4", "app:app"]