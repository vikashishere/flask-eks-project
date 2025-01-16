# # app.py
# from flask import Flask

# app = Flask(__name__)

# @app.route('/')
# def home():
#     return "Hello, World! Welcome to the Flask App deployed on EKS!"

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)


# from flask import Flask
# from prometheus_client import start_http_server, Counter, Gauge, generate_latest
# from flask import Response

# app = Flask(__name__)

# # Metrics
# REQUEST_COUNT = Counter('flask_app_requests_total', 'Total number of requests')
# ACTIVE_REQUESTS = Gauge('flask_app_active_requests', 'Number of active requests')

# @app.route('/')
# def home():
#     REQUEST_COUNT.inc()  # Increment the request count
#     return "Hello, World! Welcome to the Flask App deployed on EKS!"

# @app.route('/metrics')
# def metrics():
#     return Response(generate_latest(), mimetype="text/plain")

# if __name__ == '__main__':
#     # Start Prometheus metrics server
#     start_http_server(5001)  # Default Prometheus metrics exposed on port 5001
#     app.run(host='0.0.0.0', port=5000)

# from flask import Flask
# from prometheus_client import start_http_server, Counter

# app = Flask(__name__)

# # Define a simple metric
# REQUEST_COUNT = Counter('request_count', 'App Request Count')

# @app.route('/')
# def home():
#     REQUEST_COUNT.inc()
#     return "Hello, World! Welcome to the Flask App deployed on EKS!"

# @app.route('/metrics')
# def metrics():
#     return start_http_server(5001)

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)  # Main app listens on port 5000

from flask import Flask, jsonify
import random
import time

app = Flask(__name__)

# Simulated metrics
total_requests = 0

@app.route("/metrics", methods=["GET"])
def metrics():
    global total_requests
    total_requests += 1

    # Simulated values
    request_processing_latency = round(random.uniform(0.1, 1.5), 3)  # Latency in seconds
    model_prediction_success_rate = round(random.uniform(80, 100), 2)  # Success rate in %

    # Return the metrics in Prometheus format
    prometheus_metrics = (
        f"# HELP total_api_requests_total Total number of API requests\n"
        f"# TYPE total_api_requests_total counter\n"
        f"total_api_requests_total {total_requests}\n"
        f"\n"
        f"# HELP request_processing_latency_seconds Latency for request processing\n"
        f"# TYPE request_processing_latency_seconds gauge\n"
        f"request_processing_latency_seconds {request_processing_latency}\n"
        f"\n"
        f"# HELP model_prediction_success_rate Model prediction success rate\n"
        f"# TYPE model_prediction_success_rate gauge\n"
        f"model_prediction_success_rate {model_prediction_success_rate}\n"
    )

    return prometheus_metrics, 200, {"Content-Type": "text/plain; charset=utf-8"}

@app.route("/", methods=["GET"])
def index():
    return jsonify({"message": "Welcome to the Flask Metrics App! Access /metrics for Prometheus metrics."})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

