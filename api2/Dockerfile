FROM python:3.11-slim
WORKDIR /app
COPY app.py .
RUN pip install flask
EXPOSE 5002
CMD ["python", "app.py"]
COPY api2/app.py /app.py