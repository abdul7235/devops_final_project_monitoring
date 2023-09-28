FROM python:latest

ADD . /devops_final_project_server

WORKDIR /devops_final_project_server

RUN pip install -r requirements.txt

ENTRYPOINT ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--workers", "1"]
