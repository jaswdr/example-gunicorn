# Simple Gunicorn example

### Getting started

Build and run the container.

```bash
docker build -t example .
docker run -p 8000:8000 example
```

Then do a HTTP request to `http://localhost:8000`.

```bash
curl -i http://localhost:8000

HTTP/1.1 200 OK
Server: gunicorn
Date: Wed, 19 May 2021 08:43:56 GMT
Connection: close
Content-Type: application/json
Content-Length: 44

{"statusCode": 200, "body": "Hello, world!"}
```
