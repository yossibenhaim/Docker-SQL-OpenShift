FROM python:3.9

WORKDIR /data-loader

COPY . /data-loader

RUN pip install --no-cache-dir --upgrade -r /data-loader/requirements.txt

EXPOSE 80

CMD ["uvicorn", "services/api_server/server.py:app", "--host", "0.0.0.0","--port", "80"]