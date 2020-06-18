# Calculator API using Flask, Sqlite
## Introduction
A calculator API which stores calculations as they happen and shares those calculations with all users of that API.

For example, user A sends a request to calculate "5 + 5", which returns a response of "10". This is then streamed to all connected users as "5 + 5 = 10". Now, user B calculates "3 4". This calculates to “12” and is streamed as "3 4 = 12" right after the prior calculation. User A sees this update immediately after user B posts it.

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
**Api calls:** GET method to get Top 10 calculations, POST method to calculate given problem
```
curl http://127.0.0.1:8000/calculate -X POST -d "data=3 * 0"

curl http://127.0.0.1:8000/history -X GET
```
