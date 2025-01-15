# # app.py
# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return "Hello, World! Welcome to the Flask App deployed on EKS!"

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)


from flask import Flask
from prometheus_client import start_http_server, Counter, Gauge, generate_latest
from flask import Response

app = Flask(__name__)

# Metrics
REQUEST_COUNT = Counter('flask_app_requests_total', 'Total number of requests')
ACTIVE_REQUESTS = Gauge('flask_app_active_requests', 'Number of active requests')

@app.route('/')
def home():
    REQUEST_COUNT.inc()  # Increment the request count
    return "Hello, World! Welcome to the Flask App deployed on EKS!"

@app.route('/metrics')
def metrics():
    return Response(generate_latest(), mimetype="text/plain")

if __name__ == '__main__':
    # Start Prometheus metrics server
    start_http_server(5001)  # Default Prometheus metrics exposed on port 5001
    app.run(host='0.0.0.0', port=5000)
