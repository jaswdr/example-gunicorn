import json

def main(environ, start_response):
    """Simple example of web service using gunicorn"""
    data = json.dumps({"statusCode": 200, "body": "Hello, world!"}).encode('utf-8')
    status = "200 OK"
    start_response(status, [
            ("Content-Type", "application/json"),
            ("Content-Length", str(len(data)))
        ])
    return iter([data])

