FROM python:3.11-slim-buster

WORKDIR /app

COPY . /app

RUN python -m venv venv
ENV VIRTUAL_ENV=/app/venv
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 1323

CMD ["python", "run.py"]