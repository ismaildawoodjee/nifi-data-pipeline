FROM apache/airflow:latest-python3.8

# If I want to import `home/airflow/src`, I have to add `/home/airflow` to PYTHONPATH
ENV PYTHONPATH="${PYTHONPATH}:/home/airflow"

COPY ./requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt