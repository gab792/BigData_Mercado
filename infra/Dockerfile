FROM jupyter/scipy-notebook:latest

WORKDIR /home/jovyan/work

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8888