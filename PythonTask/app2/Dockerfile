FROM python:3.6.8
  
COPY . .

RUN apt-get update -y
RUN apt-get install python3-venv python3-pip -y

RUN python3 -m venv venv
RUN . venv/bin/activate
RUN pip3 install flask
RUN pip3 install requests

EXPOSE 5001

ENTRYPOINT ["python3","app.py"]
