FROM python:3.9-slim

WORKDIR /app

COPY report_generator.py .

RUN pip install requests

CMD ["python", "report_generator.py"]