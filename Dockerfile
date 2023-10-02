FROM python:3.10.12-alpine
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]

HEALTHCHECK --interval=30s --timeout=10s --retries=3 CMD curl -f http://localhost:5000/health || exit 1