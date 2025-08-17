FROM python:3.9

WORKDIR /data-loader

COPY . .

RUN pip install --no-cache-dir --upgrade -r /data-loader/requirements.txt


CMD ["fastapi", "run", "services/api_server/server.py", "--port", "80", "--workers", "4"]