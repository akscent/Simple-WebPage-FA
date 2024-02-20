FROM python:3.10.12

COPY . .

RUN pip install -r requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

# sudo lsof -i :80 - check port
# sudo killall nginx | PID - kill nginx process ar pid of process
# docker build . --tag fastapi_app && docker run -p 80:80 fastapi_app
