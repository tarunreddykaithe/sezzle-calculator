FROM python:3.8

WORKDIR /app 

COPY src/ /app

# Create app directory
WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 8080
CMD [ "python", "calculator.py" ]