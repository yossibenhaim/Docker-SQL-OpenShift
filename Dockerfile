FROM python:3.9

WORKDIR /data-loader

COPY services /data-loader

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 8000

CMD ["uvicorn", "/api_server/server.py:app", "--host", "0.0.0.0","--port", "8000"]