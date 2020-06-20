# Calculator API using Flask, Sqlite
## Introduction
A Calculator Webapp which stores recent calculations and shares with other users.

And also Calculator API which stores calculations as they happen and shares those calculations with all users of that API.

## Demo

**Live Web App:**

[Sezzle-Calulator Webapp](http://52.53.191.80:8080/)

**Api calls:** GET method to get Top 10 calculations, POST method to calculate given problem
```
curl http://52.53.191.80:8080/calculate -X POST -d "operation=3 * 0"
curl http://52.53.191.80:8080/calculate -X POST -d {"operation":"3 * 0"}

curl http://52.53.191.80:8080/history -X GET
```
Note: If deployed in local computer, use "localhost" instead of 52.53.191.80.

## Instructions

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
