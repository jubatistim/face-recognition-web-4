FROM python:3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
# ENTRYPOINT ["python"]
# CMD ["app.py"]
EXPOSE 80
CMD ["gunicorn", "--bind", "0.0.0.0:80", "app:app"]