FROM python:3.13-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY todo_app.py .
ENV PYTHONUNBUFFERED=1
USER nobody
CMD ["python", "todo_app.py"]
