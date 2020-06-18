#get Python Image
FROM python:3.8

# Create app directory
WORKDIR /app 

#Copy scripts from src to app
COPY src/ /app

#Install libraries from requirements.txt
RUN pip install -r requirements.txt

#Run calculator script
CMD [ "python", "calculator.py" ]