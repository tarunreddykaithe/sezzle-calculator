# Calculator API using Flask, Sqlite, AWS and Docker
## Introduction
A Calculator Webapp UI which  stores calculations as they happen and shares those calculations with all users of that API.

## Demo

**Live Web App:**

Deployed on EC2 instance using docker. Link: [Sezzle-Calulator Webapp](http://ec2-52-53-191-80.us-west-1.compute.amazonaws.com:8080/)

**Api calls:**
Both normal data and JSON data can be used in POST method to calculate given problem and GET method to get Top 10 calculations.
```
curl http://52.53.191.80:8080/calculate -X POST -d "operation=3 * 0"
curl http://52.53.191.80:8080/calculate -X POST -d '{"operation":"3 * 0"}' -H "Content-Type: application/json" 

curl http://52.53.191.80:8080/history -X GET
```
Note: If deployed in local computer, use "localhost" instead of 52.53.191.80.

## Instructions

Deployment can be done in three steps. All you have to do is clone this repository, build docker file and run it.

**Build the Application:** 
```bash
git clone https://github.com/tarunreddykaithe/sezzle-calculator.git
cd sezzle-calculator
docker build -t calculator:latest .
```
**Run the Application:** 
```bash
docker run --publish 8080:8080 --detach --name calculator calculator:latest
```
