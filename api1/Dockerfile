FROM python:3.11-slim
WORKDIR /app
COPY app.py .
RUN pip install flask requests
EXPOSE 5001
CMD ["python", "app.py"]
COPY api1/app.py /app.py